<!-- Generated from skills/catalog.json. Edit the catalog and run scripts/generate_skills.py. -->
---
name: AI project planning
description: Convert requirements into verifiable milestones, dependency-aware work items, risks and explicit assumptions.
category: ai-development
last-reviewed: 2026-11-25
---

# AI project planning

## Description
Convert requirements into verifiable milestones, dependency-aware work items, risks and explicit assumptions.

## Purpose
Use this guide to carry out the task below in a reproducible, reviewable way. It is an agent instruction set, not a claim that the external product or service is free, available in every region, or unchanged.

## When to use
- The task is specifically about ai project planning.
- The requested output can be validated against a concrete requirement and target environment.
- You are authorized to use the project, account, media, device or service involved.

## Requirements
- A clearly scoped task, success criteria, target platform and permitted inputs.
- Access to a suitable test project, fixture or copy of user data.
- Review current vendor/runtime requirements before relying on version-specific behavior.

## Supported tools
A supported language runtime, provider API/SDK if needed, test framework, structured logging and secret store. Choose the simplest tool that meets the task.

## Installation
Use the runtime's official installation method and the project's lockfile. Place provider keys in a local ignored environment file or managed secret store; never paste credentials into prompts, source, client bundles or logs.

## Step-by-step workflow
1. Define the user goal, allowed data, model/tool boundaries, budget/latency constraints and a deterministic stop condition.
2. Keep application policy and authorization in ordinary code; use schemas and runtime validation at every model/tool boundary.
3. Implement a minimal end-to-end path with timeouts, bounded retries and redacted structured logs.
4. Test normal, malformed, adversarial, timeout, provider-error and unauthorized-action cases with fixtures.
5. Inspect the complete output/actions and require human approval where the workflow can change external or user data.

### Agent workflow
Use a supported runtime and a model/provider SDK only when required. Isolate credentials in environment variables or a secret manager.

## Practical example
**Task:** Plan a small API feature with acceptance criteria and an integration test milestone.

1. Use a deterministic fake model/tool response first so the workflow can be tested without provider cost or network access.
2. Validate model/tool input against an explicit schema and keep authorization checks in application code.
3. Exercise the example with a valid request, malformed arguments, timeout and provider/tool error; assert the expected safe stop.
4. Inspect the result and logs for unintended writes, secret disclosure, unbounded loops and unauthorized side effects.

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
Model inference, APIs, GPU compute and hosting may cost money and have quotas. Never assume a model/API is unlimited or free; obtain clear user approval before any paid inference and enforce a budget in the application.

## Official documentation
- [https://platform.openai.com/docs](https://platform.openai.com/docs)
- Confirm product-specific instructions, supported versions and availability at the vendor's official documentation before relying on them.

## Verification checklist
- [ ] The requested outcome and constraints are met without unrelated changes.
- [ ] The workflow's focused example/check completed and its output was inspected.
- [ ] Relevant error, permission, edge-case and compatibility paths were considered.
- [ ] No credentials or unlicensed assets were introduced; cost and authorization limits are understood.
- [ ] The result, tested environment and any unverified assumptions are reported clearly.

## Status
**Last reviewed:** 2026-11-25. Workflow guidance reviewed for this repository; recheck official documentation and service availability before production use.
