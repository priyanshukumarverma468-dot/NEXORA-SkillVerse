"""Small standard-library OpenRouter example with explicit price gating."""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from decimal import Decimal, InvalidOperation

BASE_URL = "https://openrouter.ai/api/v1"


class OpenRouterError(RuntimeError):
    def __init__(self, message, status=None, retry_after=None):
        super().__init__(message)
        self.status = status
        self.retry_after = retry_after


def _zero_priced(pricing):
    if not isinstance(pricing, dict) or not {"prompt", "completion"} <= pricing.keys():
        return False
    values = []
    for value in pricing.values():
        if value is None:
            return False
        try:
            price = Decimal(str(value))
        except (InvalidOperation, ValueError):
            return False
        if not price.is_finite():
            return False
        values.append(price)
    return bool(values) and all(value == 0 for value in values)


class OpenRouterClient:
    def __init__(self, api_key, timeout=30, opener=None):
        if not api_key:
            raise ValueError("An API key is required for inference")
        self.api_key = api_key
        self.timeout = timeout
        self.opener = opener or urllib.request.urlopen
        self.usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        self.estimated_cost = Decimal(0)

    def _request_json(self, path, payload=None):
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        headers = {"Accept": "application/json"}
        if payload is not None:
            headers["Content-Type"] = "application/json"
        if path.split("?", 1)[0] != "/models":
            headers["Authorization"] = f"Bearer {self.api_key}"
        request = urllib.request.Request(BASE_URL + path, data=data, headers=headers)
        try:
            with self.opener(request, timeout=self.timeout) as response:
                body = response.read()
        except urllib.error.HTTPError as error:
            status = error.code
            retry_after = error.headers.get("Retry-After") if error.headers else None
            error.close()
            raise OpenRouterError(
                f"OpenRouter returned HTTP {status}",
                status=status,
                retry_after=retry_after,
            ) from None
        except urllib.error.URLError as error:
            raise OpenRouterError(f"OpenRouter network error: {error.reason}") from None
        try:
            result = json.loads(body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            raise OpenRouterError("OpenRouter returned invalid JSON") from None
        if not isinstance(result, dict):
            raise OpenRouterError("OpenRouter returned an unexpected response shape")
        if result.get("error"):
            error = result["error"]
            message = error.get("message", "Request failed") if isinstance(error, dict) else "Request failed"
            raise OpenRouterError(f"OpenRouter API error: {message}", status=400)
        return result

    def list_models(self):
        models = []
        offset = 0
        page_size = 1000
        while True:
            response = self._request_json(f"/models?limit={page_size}&offset={offset}")
            page = response.get("data")
            if not isinstance(page, list):
                raise OpenRouterError("Model catalog response has no data list")
            models.extend(model for model in page if isinstance(model, dict) and isinstance(model.get("id"), str))
            if len(page) < page_size:
                return models
            offset += page_size

    def complete(self, model_ids, prompt, approved_paid_ids=(), max_tokens=512):
        if not isinstance(model_ids, (list, tuple)) or not model_ids:
            raise ValueError("Provide a non-empty list of explicit model IDs")
        if not all(isinstance(model_id, str) and model_id for model_id in model_ids):
            raise ValueError("Every model ID must be a non-empty string")
        if len(set(model_ids)) != len(model_ids):
            raise ValueError("Provide a non-empty list of unique, explicit model IDs")
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("Prompt must not be empty")
        if not isinstance(max_tokens, int) or isinstance(max_tokens, bool) or max_tokens < 1:
            raise ValueError("max_tokens must be a positive integer")
        approved_paid_ids = set(approved_paid_ids)
        catalog = {model["id"]: model for model in self.list_models()}
        candidates = []
        for model_id in model_ids:
            model = catalog.get(model_id)
            if model is None:
                raise ValueError(f"Model {model_id!r} is not in the current catalog")
            if not _zero_priced(model.get("pricing")) and model_id not in approved_paid_ids:
                raise PermissionError(
                    f"Model {model_id!r} is not verified zero-priced; approval for this exact paid model is required"
                )
            candidates.append(model)

        last_error = None
        fallback_reason = None
        for index, model in enumerate(candidates):
            try:
                response = self._request_json(
                    "/chat/completions",
                    {
                        "model": model["id"],
                        "messages": [{"role": "user", "content": prompt}],
                        "max_tokens": max_tokens,
                        "stream": False,
                    },
                )
                choices = response.get("choices")
                if not isinstance(choices, list) or not choices:
                    raise OpenRouterError("Completion response contains no choices")
                message = choices[0].get("message", {})
                content = message.get("content") if isinstance(message, dict) else None
                if not isinstance(content, str):
                    raise OpenRouterError("Completion response contains no text content")
                usage = response.get("usage", {})
                usage = usage if isinstance(usage, dict) else {}
                for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
                    value = usage.get(key)
                    if isinstance(value, int) and not isinstance(value, bool):
                        self.usage[key] += value
                estimate = None
                pricing = model.get("pricing", {})
                prompt_tokens = usage.get("prompt_tokens")
                completion_tokens = usage.get("completion_tokens")
                try:
                    if (
                        isinstance(prompt_tokens, int) and not isinstance(prompt_tokens, bool)
                        and isinstance(completion_tokens, int) and not isinstance(completion_tokens, bool)
                    ):
                        prompt_rate = Decimal(str(pricing["prompt"]))
                        completion_rate = Decimal(str(pricing["completion"]))
                        if prompt_rate.is_finite() and completion_rate.is_finite():
                            estimate = prompt_rate * prompt_tokens + completion_rate * completion_tokens
                            self.estimated_cost += estimate
                except (KeyError, InvalidOperation, TypeError, ValueError):
                    estimate = None
                return {
                    "model": response.get("model", model["id"]),
                    "text": content,
                    "usage": usage,
                    "reported_cost": usage.get("cost"),
                    "catalog_cost_estimate": str(estimate) if estimate is not None else None,
                    "fallback_used": index > 0,
                    "fallback_reason": fallback_reason,
                }
            except OpenRouterError as error:
                last_error = error
                retryable = error.status is None or error.status in (404, 408, 429, 500, 502, 503, 504)
                if not retryable or index == len(candidates) - 1:
                    raise
                fallback_reason = {"status": error.status, "retry_after": error.retry_after}
        raise last_error


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", help="list explicit zero-priced catalog entries")
    parser.add_argument("--model", action="append", default=[], help="primary model followed by approved fallback IDs")
    parser.add_argument(
        "--approve-paid-model",
        action="append",
        default=[],
        help="exact paid model ID approved by the user, repeat for each paid fallback",
    )
    parser.add_argument("--prompt", help="prompt to submit; use only non-sensitive test data")
    args = parser.parse_args(argv)

    if args.discover:
        request = urllib.request.Request(BASE_URL + "/models", headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                catalog = json.loads(response.read())
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as error:
            print(f"Catalog discovery failed: {error}", file=sys.stderr)
            return 1
        for model in catalog.get("data", []):
            if isinstance(model, dict) and _zero_priced(model.get("pricing")):
                architecture = model.get("architecture")
                modalities = architecture.get("input_modalities") if isinstance(architecture, dict) else None
                print(
                    f"{model.get('id')}\t{model.get('name')}"
                    f"\tcontext={model.get('context_length')}"
                    f"\tmodalities={modalities}"
                    f"\tpricing={json.dumps(model.get('pricing'), sort_keys=True)}"
                )
        return 0

    if not args.model or args.prompt is None:
        parser.error("inference requires --model, --prompt and OPENROUTER_API_KEY")
    try:
        client = OpenRouterClient(os.environ.get("OPENROUTER_API_KEY"))
        result = client.complete(args.model, args.prompt, approved_paid_ids=args.approve_paid_model)
    except (OpenRouterError, ValueError, PermissionError) as error:
        retry = f" Retry-After: {error.retry_after}." if isinstance(error, OpenRouterError) and error.retry_after else ""
        print(f"Request failed: {error}.{retry}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    print(f"Cumulative token usage: {client.usage}", file=sys.stderr)
    print(f"Cumulative catalog cost estimate: {client.estimated_cost} (not a bill)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
