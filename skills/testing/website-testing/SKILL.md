<!-- Generated from skills/catalog.json. Edit the catalog and run scripts/generate_skills.py. -->
---
name: Website testing
description: Validate core journeys, accessibility basics, console/network errors and production-like builds.
category: testing
last-reviewed: 2026-11-25
---

# Website testing

## Description
Validate core journeys, accessibility basics, console/network errors and production-like builds.

## Purpose
Use this guide to carry out the task below in a reproducible, reviewable way. It is an agent instruction set, not a claim that the external product or service is free, available in every region, or unchanged.

## When to use
- The task is specifically about website testing.
- The requested output can be validated against a concrete requirement and target environment.
- You are authorized to use the project, account, media, device or service involved.

## Requirements
- A clearly scoped task, success criteria, target platform and permitted inputs.
- Access to a suitable test project, fixture or copy of user data.
- Review current vendor/runtime requirements before relying on version-specific behavior.

## Supported tools
The repository's test runner, static analysis and observability tools; device/browser matrix as applicable.

## Installation
Use the project's existing test commands. Install additional tools only when the project already declares them or a concrete missing check requires them.

## Step-by-step workflow
1. Translate the requirement into observable pass/fail criteria and identify the changed code paths and supported targets.
2. Select representative fixtures and a controlled environment; protect production data and redact secrets/personal data.
3. Reproduce failures with the narrowest check and save relevant command, environment and evidence.
4. Confirm the root cause, add or update a regression test, and run targeted plus relevant compatibility/regression checks.
5. Report actual results, skipped coverage, environment limits and remaining uncertainty without claiming unrun tests passed.

### Testing workflow
Use the project's existing test and analysis tools. Run against controlled fixtures or staging data, not production unless explicitly authorized.

## Practical example
**Task:** Test sign-up validation and navigation against a local test deployment.

1. Turn the example into explicit pass/fail assertions and use a representative fixture that contains no production secrets or personal data.
2. Run the narrowest test first and record the exact command, runtime/device/browser and failure evidence.
3. After a fix, add a regression assertion that fails on the original defect and run related compatibility/smoke checks.
4. Report the observed result, coverage not run, and any environmental limits; do not claim a check passed if it was not run.

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
Local test tools may be free/open source, but hosted device/browser farms, commercial scanners and test data services can incur charges. Check license and service terms; test only authorized targets.

## Official documentation
- [https://testing.googleblog.com/](https://testing.googleblog.com/)
- Confirm product-specific instructions, supported versions and availability at the vendor's official documentation before relying on them.

## Verification checklist
- [ ] The requested outcome and constraints are met without unrelated changes.
- [ ] The workflow's focused example/check completed and its output was inspected.
- [ ] Relevant error, permission, edge-case and compatibility paths were considered.
- [ ] No credentials or unlicensed assets were introduced; cost and authorization limits are understood.
- [ ] The result, tested environment and any unverified assumptions are reported clearly.

## Status
**Last reviewed:** 2026-11-25. Workflow guidance reviewed for this repository; recheck official documentation and service availability before production use.
