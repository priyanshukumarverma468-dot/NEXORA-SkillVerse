---
name: OpenRouter API integration and model routing
description: Discover current OpenRouter models, select cost-aware candidates, route requests with explicit fallback and track usage without silently authorizing paid inference.
category: ai-api-models
last-reviewed: 2026-11-25
---

# OpenRouter API integration and model routing

## Description
Build server-side applications and agents on OpenRouter's unified API. This guide covers current catalog discovery, free/paid classification, model selection, safe fallback, rate limits, context sizing, usage accounting and API-key protection.

## Purpose
Use OpenRouter as a provider boundary while keeping model choice, price approval and failure behavior understandable to the user. Model availability, pricing, limits and API features are dynamic; query the live catalog and recheck official documentation before deployment.

## When to use
- An application needs to call one or more OpenRouter models.
- A user wants to compare models for coding, reasoning, latency, context or cost.
- An agent needs explicit provider/model fallback and usage reporting.
- A service needs to distinguish free catalog entries from paid entries.

## Requirements
- An OpenRouter account and API key for authenticated inference; keep it on a trusted server.
- A language runtime with HTTPS and JSON support. The runnable example uses Python's standard library and has no package dependency.
- A task-specific acceptance set: quality, input modality, output length, context needs, latency, privacy, and maximum approved cost.
- Test prompts that do not contain personal, confidential or production data.

## Supported tools
- OpenRouter REST API: `https://openrouter.ai/api/v1`.
- `GET /models` for live model metadata including model IDs, modality, context length, supported parameters and pricing.
- `POST /chat/completions` for a broadly compatible chat request. The Responses API and supported parameters vary by model; use the current API docs.
- Optional: `curl`, Python 3.10+ and a server-side secret manager.

## Installation
1. Create an API key in the OpenRouter account interface. Review account credits, key limits and billing state first.
2. Provide the key to a server process via a secret manager or an ignored local environment file:
   ```sh
   export OPENROUTER_API_KEY='your-key-from-a-secret-store'
   ```
3. Do not commit the value, put it in a browser/mobile bundle, or print it in logs. Rotate a key if it is exposed.
4. The example implementation and tests are in [`examples/openrouter_client.py`](../../../examples/openrouter_client.py) and [`examples/test_openrouter_client.py`](../../../examples/test_openrouter_client.py).

## Step-by-step workflow
1. **Discover now, do not hard-code availability.** Fetch `/models` and inspect `id`, `name`, `context_length`, `architecture`, `supported_parameters`, `endpoints` and all relevant `pricing` fields. Catalog values and provider availability can change.
2. **Classify price conservatively.** A model is considered free by the example only when the current metadata has explicit zero prompt and completion prices and every reported pricing field is numeric zero. Unknown or missing pricing is not free. A `:free` model variant has its own limits; check its own catalog entry.
3. **Compare candidates using the task.** Test the same sanitized prompt and output contract. Compare observed quality, supported modality/tools, context, latency, provider availability and current prices. Coding model labels are not a guarantee; validate with representative repository tasks.
4. **Select an explicit ordered list.** Specify the primary and allowed fallbacks. Each candidate is checked against the live catalog. Paid candidates are rejected unless a user has explicitly approved paid use in the application flow. Never append a paid model as a hidden fallback.
5. **Bound request size and output.** Estimate input/output tokens with a model-appropriate tokenizer when precision matters. Reserve output capacity under the model's current context limit; count system instructions, tool schemas, history and multimodal payloads too. Truncate or summarize deliberately rather than silently dropping the newest task.
6. **Call server-side and handle failures.** Use HTTPS, request timeouts, validate the response shape, and surface provider/model errors. On throttling, respect `Retry-After` if present; bound retries with backoff and jitter. Only switch to a pre-approved fallback, and report which model actually answered.
7. **Record usage.** Capture returned prompt/completion/total tokens, response ID, actual model and provider metadata if returned. Track reported cost when available; otherwise label a catalog-price calculation as an estimate and disclose excluded charges. Reconcile against OpenRouter's usage/activity dashboard.
8. **Verify and monitor.** Test free and paid approval paths, rate limiting, unavailable models, malformed responses, context overflow, timeout and secret redaction before deploying.

## Practical examples

### Discover current zero-priced entries (no key required for the public catalog)
```sh
curl --fail --silent --show-error https://openrouter.ai/api/v1/models |
  jq -r '.data[] | select(.pricing.prompt == "0" and .pricing.completion == "0") |
    [.id, .name, (.context_length|tostring), (.pricing|tojson)] | @tsv'
```
This is a discovery filter, not an assurance of unlimited use or zero ancillary charges. Inspect every pricing field and the model's own limits in the official catalog before relying on it.

### Make a server-side request
```sh
curl --fail --silent --show-error https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "provider/model-id-from-live-catalog",
    "messages": [{"role":"user","content":"Reply with the word ready."}],
    "max_tokens": 16,
    "stream": false
  }'
```
Replace the model ID with a currently listed entry. Do not treat this example ID slot as a recommendation. For more complete extraction, error handling, price gating, explicit fallback and usage tracking, run:
```sh
python -m unittest examples.test_openrouter_client
python examples/openrouter_client.py --discover
```
To send a request, set `OPENROUTER_API_KEY` and pass an explicit primary model ID. By default the example permits only zero-priced candidates. Paid usage requires `--approve-paid-model 'exact/model-id'` for each paid candidate, and only after a user-facing approval step that shows the model and current price. The option is not an approval UI or spend limit by itself.

## Common errors
- **401/403:** Missing, invalid, revoked or insufficiently scoped key. Check server secret configuration and key status; do not print the key to debug it.
- **402 / insufficient credits:** Account funding or billing condition. Stop; explain the cost and require explicit user approval before any paid use.
- **429:** Rate limit or capacity restriction. Honor `Retry-After` where returned, apply bounded backoff, reduce concurrency, or use only a pre-approved fallback.
- **400 / unsupported parameter:** Model-specific API/parameter mismatch. Re-read the current model metadata and supported parameter list; do not blindly retry another paid model.
- **404 / unavailable model:** Refresh `/models`, check the exact model ID and endpoint compatibility, and present an explicit fallback choice.
- **Context-length error:** Include all messages, tool schemas, history and output tokens in the estimate; summarize or ask the user before dropping context.
- **Unexpected charge:** Stop automatic requests, inspect actual model and usage records, revoke or limit the key if needed, and investigate hidden fallback/routing behavior.

## Troubleshooting
1. Reproduce using a short, non-sensitive prompt and one explicitly selected model.
2. Record HTTP status, sanitized provider error, request/response ID, model ID and timestamp; do not log authorization headers or full private prompts.
3. Refresh model metadata and check the official model page and endpoint details; availability and pricing may have changed.
4. Distinguish provider throttling, account/key limits, model incompatibility, network failure and application validation errors.
5. If fallback is enabled, verify each candidate's current price and API compatibility, and expose the model actually selected to the caller.

## Security considerations
- Keep API keys exclusively on a trusted backend/worker. Never include a key in frontend code, mobile APKs, source control, error messages or telemetry.
- Use separate keys/projects where possible, restrict spend/permissions where supported, monitor activity and rotate promptly after exposure.
- Treat prompts, completions and tool arguments as untrusted. Validate tool inputs and keep authorization decisions outside the model.
- Minimize sensitive data sent to third-party providers; review data retention, provider routing and applicable privacy terms for each model.
- Do not automatically execute generated code or tool calls. Require scoped approval for filesystem writes, external messages, purchases, account changes and destructive operations.

## Free and paid limitations
- OpenRouter is a gateway, not a promise of free or unlimited inference. Free variants have their own rate limits, provider capacity and availability; account requirements and limits can change.
- A model's displayed price may be nonzero even when a similarly named `:free` variant exists. Compare the exact catalog entry chosen for the request.
- Paid models consume credits or can incur provider/BYOK charges. Never switch from free to paid without clear, prior user approval; approval should include the model/price basis and spending limit.
- Cost estimates based on catalog per-token prices can differ from actual charges and may omit image/audio, request, provider or other fees. Prefer returned usage/cost data when documented, then reconcile in the dashboard.
- Free availability, prices and plan terms are dynamic. Check current catalog, [pricing](https://openrouter.ai/pricing), [FAQ](https://openrouter.ai/docs/faq) and account limits at use time.

## Official documentation
- [OpenRouter documentation](https://openrouter.ai/docs)
- [Quickstart](https://openrouter.ai/docs/quickstart)
- [Models API reference](https://openrouter.ai/docs/api/api-reference/models/list-all-models-and-their-properties)
- [Live model catalog](https://openrouter.ai/api/v1/models)
- [Free model variant details](https://openrouter.ai/docs/guides/routing/model-variants/free)
- [Provider selection and routing](https://openrouter.ai/docs/guides/routing/provider-selection)
- [FAQ: pricing, rate limits and models](https://openrouter.ai/docs/faq)
- [Usage dashboard](https://openrouter.ai/activity)

## Verification checklist
- [ ] Catalog discovery succeeds and malformed/unpriced metadata is not classified as free.
- [ ] The chosen ID supports the intended endpoint, modality, context and parameters.
- [ ] Paid candidates are blocked unless that exact model ID has an explicit user approval signal.
- [ ] Fallback targets are configured in advance, price-checked and reported when used.
- [ ] 401, 402, 429, 5xx, timeout, malformed JSON and context-overflow paths fail visibly.
- [ ] API keys and private prompts are absent from client bundles, source control and logs.
- [ ] Token counts and any cost estimate are labeled accurately and reconciled with dashboard data.
- [ ] Tests pass without network access: `python -m unittest examples.test_openrouter_client`.

## Status
**Last reviewed:** 2026-11-25. The official quickstart, FAQ and model API reference were checked on this date; model availability, pricing, quotas and endpoint support must be refreshed at runtime.
