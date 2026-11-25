<!-- Generated from skills/catalog.json. Edit the catalog and run scripts/generate_skills.py. -->
---
name: Git
description: Use small reviewable commits, inspect status and diffs, and recover safely without discarding unrelated work.
category: programming
last-reviewed: 2026-11-25
---

# Git

## Description
Use small reviewable commits, inspect status and diffs, and recover safely without discarding unrelated work.

## Purpose
Use this guide to carry out the task below in a reproducible, reviewable way. It is an agent instruction set, not a claim that the external product or service is free, available in every region, or unchanged.

## When to use
- The task is specifically about git.
- The requested output can be validated against a concrete requirement and target environment.
- You are authorized to use the project, account, media, device or service involved.

## Requirements
- A clearly scoped task, success criteria, target platform and permitted inputs.
- Access to a suitable test project, fixture or copy of user data.
- Review current vendor/runtime requirements before relying on version-specific behavior.

## Supported tools
The language runtime/compiler and formatter, linter and test runner already used by the repository.

## Installation
Use the project's declared version manager, package manifest and lockfile. If starting from scratch, follow the language or framework's official quickstart and pin a supported version.

## Step-by-step workflow
1. Identify the actual runtime/compiler version, entry point, module system, conventions and existing tests before editing.
2. Define input/output behavior and edge cases; use the language's native validation, error handling and type system.
3. Make a minimal implementation that follows nearby patterns; do not introduce a dependency for functionality already available.
4. Add a focused test for the requested behavior and at least one meaningful boundary/error case.
5. Run the smallest relevant formatter, static check and test command; inspect the diff and report any unrun checks.

### Development workflow
Use the repository's existing runtime, package manager, formatter and test runner. Install dependencies only when required and document required versions.

## Practical example
**Task:** Create a feature branch, stage only intended files and inspect the staged diff.

1. Implement only the example task in the project's existing language version and module structure; validate untrusted input at the boundary.
2. Stage paths explicitly, inspect `git diff --cached`, then commit only the requested change; do not use a destructive reset to clean unrelated work.
3. Add one success test and a boundary/error test using the current test framework; do not add a package just to demonstrate the feature.
4. Run the existing formatter/linter and smallest relevant test command, then inspect the changed file and final diff.
5. Compare actual behavior with the example's requirement and report commands, output and any unverified runtime assumptions.

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
Many language toolchains are free/open source, but IDE features, commercial libraries, hosted services and deployment can cost money. Check each dependency's license and service plan before use.

## Official documentation
- [https://git-scm.com/doc](https://git-scm.com/doc)
- Confirm product-specific instructions, supported versions and availability at the vendor's official documentation before relying on them.

## Verification checklist
- [ ] The requested outcome and constraints are met without unrelated changes.
- [ ] The workflow's focused example/check completed and its output was inspected.
- [ ] Relevant error, permission, edge-case and compatibility paths were considered.
- [ ] No credentials or unlicensed assets were introduced; cost and authorization limits are understood.
- [ ] The result, tested environment and any unverified assumptions are reported clearly.

## Status
**Last reviewed:** 2026-11-25. Workflow guidance reviewed for this repository; recheck official documentation and service availability before production use.
