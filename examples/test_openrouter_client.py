import io
import json
import unittest
import urllib.error

from examples.openrouter_client import OpenRouterClient, OpenRouterError


class FakeResponse:
    def __init__(self, payload):
        self.body = json.dumps(payload).encode()

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self.body


class OpenRouterClientTests(unittest.TestCase):
    def make_client(self, models, completions):
        queue = [FakeResponse({"data": models})] + [FakeResponse(item) for item in completions]

        def opener(_request, timeout):
            self.assertEqual(timeout, 30)
            return queue.pop(0)

        return OpenRouterClient("test-key", opener=opener)

    def test_free_model_completion_tracks_usage(self):
        client = self.make_client(
            [{"id": "test/free", "pricing": {"prompt": "0", "completion": "0"}}],
            [{
                "model": "test/free",
                "choices": [{"message": {"content": "ready"}}],
                "usage": {"prompt_tokens": 3, "completion_tokens": 1, "total_tokens": 4},
            }],
        )
        result = client.complete(["test/free"], "Say ready")
        self.assertEqual(result["text"], "ready")
        self.assertFalse(result["fallback_used"])
        self.assertEqual(client.usage["total_tokens"], 4)

    def test_paid_candidate_requires_explicit_approval(self):
        client = self.make_client(
            [{"id": "test/paid", "pricing": {"prompt": "0.01", "completion": "0.02"}}],
            [],
        )
        with self.assertRaises(PermissionError):
            client.complete(["test/paid"], "test")

    def test_paid_approval_is_specific_to_model_id(self):
        client = self.make_client(
            [{"id": "test/paid", "pricing": {"prompt": "0.01", "completion": "0.02"}}],
            [{
                "model": "test/paid",
                "choices": [{"message": {"content": "approved"}}],
                "usage": {"prompt_tokens": 2, "completion_tokens": 1, "total_tokens": 3},
            }],
        )
        result = client.complete(["test/paid"], "test", approved_paid_ids={"test/paid"})
        self.assertEqual(result["text"], "approved")
        self.assertEqual(result["catalog_cost_estimate"], "0.04")

    def test_fallback_is_explicit_and_reports_actual_model(self):
        models = [
            {"id": "test/primary", "pricing": {"prompt": "0", "completion": "0"}},
            {"id": "test/fallback", "pricing": {"prompt": "0", "completion": "0"}},
        ]
        queue = [FakeResponse({"data": models})]

        def opener(request, timeout):
            if request.full_url.endswith("/chat/completions"):
                payload = json.loads(request.data)
                if payload["model"] == "test/primary":
                    raise urllib.error.HTTPError(
                        request.full_url, 429, "limited", {"Retry-After": "2"}, io.BytesIO()
                    )
                return FakeResponse({
                    "model": "test/fallback",
                    "choices": [{"message": {"content": "ok"}}],
                    "usage": {},
                })
            return queue.pop(0)

        client = OpenRouterClient("test-key", opener=opener)
        result = client.complete(["test/primary", "test/fallback"], "test")
        self.assertEqual(result["model"], "test/fallback")
        self.assertTrue(result["fallback_used"])
        self.assertEqual(result["fallback_reason"], {"status": 429, "retry_after": "2"})

    def test_unknown_price_is_not_treated_as_free(self):
        client = self.make_client(
            [{"id": "test/unknown", "pricing": {"prompt": "0", "completion": None}}],
            [],
        )
        with self.assertRaises(PermissionError):
            client.complete(["test/unknown"], "test")

    def test_paid_fallback_is_checked_before_primary_request(self):
        models = [
            {"id": "test/free", "pricing": {"prompt": "0", "completion": "0"}},
            {"id": "test/paid", "pricing": {"prompt": "0.01", "completion": "0.02"}},
        ]
        queue = [FakeResponse({"data": models})]
        completion_attempts = []

        def opener(request, timeout):
            if request.full_url.endswith("/chat/completions"):
                completion_attempts.append(request)
            return queue.pop(0)

        client = OpenRouterClient("test-key", opener=opener)
        with self.assertRaises(PermissionError):
            client.complete(["test/free", "test/paid"], "test")
        self.assertEqual(completion_attempts, [])

    def test_model_catalog_paginates(self):
        first_page = [{"id": f"test/model-{index}"} for index in range(1000)]
        second_page = [{"id": "test/model-1000"}]
        queue = [FakeResponse({"data": first_page}), FakeResponse({"data": second_page})]
        requested_urls = []

        def opener(request, timeout):
            requested_urls.append(request.full_url)
            return queue.pop(0)

        client = OpenRouterClient("test-key", opener=opener)
        models = client.list_models()
        self.assertEqual(len(models), 1001)
        self.assertIn("offset=0", requested_urls[0])
        self.assertIn("offset=1000", requested_urls[1])

    def test_non_retryable_http_error_does_not_fallback(self):
        models = [
            {"id": "test/primary", "pricing": {"prompt": "0", "completion": "0"}},
            {"id": "test/fallback", "pricing": {"prompt": "0", "completion": "0"}},
        ]
        queue = [FakeResponse({"data": models})]
        attempts = []

        def opener(request, timeout):
            if request.full_url.endswith("/chat/completions"):
                attempts.append(request.data)
                raise urllib.error.HTTPError(request.full_url, 400, "bad request", {}, io.BytesIO())
            return queue.pop(0)

        client = OpenRouterClient("test-key", opener=opener)
        with self.assertRaises(OpenRouterError):
            client.complete(["test/primary", "test/fallback"], "test")
        self.assertEqual(len(attempts), 1)


if __name__ == "__main__":
    unittest.main()
