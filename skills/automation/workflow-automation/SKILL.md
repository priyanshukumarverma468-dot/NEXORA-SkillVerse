<!-- Generated from skills/catalog.json. Edit the catalog and run scripts/generate_skills.py. -->
---
name: Workflow automation
description: Connect workflow steps with validated inputs, idempotency, retries and human approval for consequential actions.
category: automation
last-reviewed: 2026-11-25
---

# Workflow automation

## Description
Connect workflow steps with validated inputs, idempotency, retries and human approval for consequential actions.

## Purpose
Use this guide to carry out the task below in a reproducible, reviewable way. It is an agent instruction set, not a claim that the external product or service is free, available in every region, or unchanged.

## When to use
- The task is specifically about workflow automation.
- The requested output can be validated against a concrete requirement and target environment.
- You are authorized to use the project, account, media, device or service involved.

## Requirements
- A clearly scoped task, success criteria, target platform and permitted inputs.
- Access to a suitable test project, fixture or copy of user data.
- Review current vendor/runtime requirements before relying on version-specific behavior.

## Supported tools
Playwright or Selenium for browser work; otherwise the narrowest vendor SDK/CLI and an isolated test target.

## Installation
Use the repository's pinned runtime and browser dependencies. Install Playwright/Selenium only when selected by the project; use a local test server or vendor sandbox before a live target.

## Step-by-step workflow
1. Confirm written authorization, the exact target/environment, allowed actions, rate limits and data handling rules.
2. Prefer stable semantic locators/API contracts over coordinates or fragile DOM structure; never attempt access-control bypass.
3. Use test identities and fixtures; add timeouts, idempotency safeguards, explicit retry conditions and a dry-run where feasible.
4. Run a single bounded test, collect trace/log/screenshot evidence and verify resulting state before expanding the run.
5. Require human confirmation before sending messages, publishing, purchases, account changes, deletes or other consequential actions.

### Automation workflow
Use a supported automation runtime and a test/staging target. Provide only the permissions needed for the defined task.

## Practical example
**Task:** Automate a test ticket routing flow and retain an execution log.

1. Run against a local fixture or staging target with a test identity; verify the exact hostname and allowed actions first.
2. Prefer role/label/API locators, set a bounded timeout and capture trace or sanitized logs on failure.
3. Execute one dry-run or read-only test and verify the resulting state before allowing any write action.
4. Test duplicate invocation, timeout and retry behavior; require human confirmation for external messages or irreversible changes.

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
Automation frameworks may be free/open source, while hosted browsers, device farms, proxy services and target platforms can charge or restrict use. Confirm authorization, terms and current quotas.

## Official documentation
- [https://playwright.dev/docs/intro](https://playwright.dev/docs/intro)
- Confirm product-specific instructions, supported versions and availability at the vendor's official documentation before relying on them.

## Verification checklist
- [ ] The requested outcome and constraints are met without unrelated changes.
- [ ] The workflow's focused example/check completed and its output was inspected.
- [ ] Relevant error, permission, edge-case and compatibility paths were considered.
- [ ] No credentials or unlicensed assets were introduced; cost and authorization limits are understood.
- [ ] The result, tested environment and any unverified assumptions are reported clearly.

## Status
**Last reviewed:** 2026-11-25. Workflow guidance reviewed for this repository; recheck official documentation and service availability before production use.
