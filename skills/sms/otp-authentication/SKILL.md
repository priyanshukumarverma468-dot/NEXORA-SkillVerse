<!-- Generated from skills/catalog.json. Edit the catalog and run scripts/generate_skills.py. -->
---
name: OTP authentication
description: Implement short-lived, single-use OTP verification with rate limits, secure storage and abuse controls.
category: sms
last-reviewed: 2026-11-25
---

# OTP authentication

## Description
Implement short-lived, single-use OTP verification with rate limits, secure storage and abuse controls.

## Purpose
Use this guide to carry out the task below in a reproducible, reviewable way. It is an agent instruction set, not a claim that the external product or service is free, available in every region, or unchanged.

## When to use
- The task is specifically about otp authentication.
- The requested output can be validated against a concrete requirement and target environment.
- You are authorized to use the project, account, media, device or service involved.

## Requirements
- A clearly scoped task, success criteria, target platform and permitted inputs.
- Access to a suitable test project, fixture or copy of user data.
- Review current vendor/runtime requirements before relying on version-specific behavior.

## Supported tools
A regional SMS provider account/API, server-side runtime, queue/worker if asynchronous delivery is needed, and verified test recipient.

## Installation
Create a provider account and complete any identity/sender verification required in your target region. Review current per-message fees and test-mode restrictions before enabling sends.

## Step-by-step workflow
1. Confirm the recipient opted in, the use is lawful, and sender registration and delivery rules for the destination country.
2. Keep provider API calls on a trusted server; never send API secrets to a browser or mobile application.
3. Use cryptographically secure, short-lived, single-use codes when implementing OTP; store a keyed hash rather than a reusable plaintext code.
4. Apply resend and verification limits per account, destination and network signal; avoid exposing whether an account/number exists.
5. Test provider status callbacks, delayed/failed delivery and user opt-out; inspect actual provider charges before launch.

### Messaging workflow
Use an account and sender approved for the target region. Store provider credentials server-side and use the provider's test mode where available.

## Practical example
**Task:** Verify a test OTP, then assert replay and expired-code attempts fail.

1. Use the provider's sandbox/test mode and a recipient that has explicitly consented; do not use a real OTP to test production access.
2. Send one test request from a server-side process and retain the provider message ID/status without logging the secret or full phone number.
3. Test invalid destination, opt-out, resend throttling, delayed status callback and duplicate job delivery.
4. Review the provider's current destination-specific price and sender rules before enabling real traffic.

## Common errors
- **Wrong target or version:** Confirm the selected project, app, runtime, account, platform and installed tool version before changing configuration.
- **Unreproducible failure:** Save the exact command, sanitized error, environment/version details and minimal input; reproduce before attempting a fix.
- **Success reported without evidence:** Check the produced artifact/state directly. A successful command exit alone does not prove correct user-facing behavior.
- **Unexpected cost or permission:** Stop the operation, inspect the configured plan/permissions and obtain approval before continuing.

## Troubleshooting
1. Reproduce the issue with the smallest safe input in a test environment.
2. Read the first actionable error and nearby logs; redact credentials, personal data and tokens.
3. Check current official documentation for version, platform, quota and configuration changes.
4. Change one variable at a time, rerun the focused example and preserve a rollback path.
5. If unresolved, report evidence and the exact missing prerequisite rather than guessing.

## Security considerations
- Use only authorized projects, accounts, devices, media and data; ask before performing actions outside the stated scope.
- Minimize permissions and data collection; keep credentials in a secret manager or ignored local environment file.
- Treat user-supplied content, model output, downloaded files and third-party actions as untrusted.
- Use licensed software/assets and follow applicable privacy, platform and regional requirements.

## Free and paid limitations
SMS is not universally free. Pricing, sender registration, verification, regional coverage and local regulations vary; obtain current provider terms and user consent.

## Official documentation
- [https://www.twilio.com/docs/sms](https://www.twilio.com/docs/sms)
- Confirm product-specific instructions, supported versions and availability at the vendor's official documentation before relying on them.

## Verification checklist
- [ ] The requested outcome and constraints are met without unrelated changes.
- [ ] The workflow's focused example/check completed and its output was inspected.
- [ ] Relevant error, permission, edge-case and compatibility paths were considered.
- [ ] No credentials or unlicensed assets were introduced; cost and authorization limits are understood.
- [ ] The result, tested environment and any unverified assumptions are reported clearly.

## Status
**Last reviewed:** 2026-11-25. Workflow guidance reviewed for this repository; recheck official documentation and service availability before production use.
