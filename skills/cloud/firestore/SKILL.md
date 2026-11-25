<!-- Generated from skills/catalog.json. Edit the catalog and run scripts/generate_skills.py. -->
---
name: Cloud Firestore
description: Model Firestore documents and queries around access patterns, security rules, indexes and cost-aware reads.
category: cloud
last-reviewed: 2026-11-25
---

# Cloud Firestore

## Description
Model Firestore documents and queries around access patterns, security rules, indexes and cost-aware reads.

## Purpose
Use this guide to carry out the task below in a reproducible, reviewable way. It is an agent instruction set, not a claim that the external product or service is free, available in every region, or unchanged.

## When to use
- The task is specifically about cloud firestore.
- The requested output can be validated against a concrete requirement and target environment.
- You are authorized to use the project, account, media, device or service involved.

## Requirements
- A clearly scoped task, success criteria, target platform and permitted inputs.
- Access to a suitable test project, fixture or copy of user data.
- Review current vendor/runtime requirements before relying on version-specific behavior.

## Supported tools
Vendor CLI/console, SDK or REST API; local emulator/preview environment where provided; Git and a test identity.

## Installation
Create or select a vendor account/project, install the vendor's official CLI/SDK only if needed, and configure a non-production project. Check current free-tier, quota, regional and billing settings before provisioning.

## Step-by-step workflow
1. Confirm vendor, region, account, environment, service availability, current quotas and whether billing is enabled.
2. Model identity, data access, retention and recovery before creating resources; use a disposable development project.
3. Configure credentials through environment bindings/secret managers and implement the narrowest service policy.
4. Test allowed and denied operations with separate test identities, then inspect logs and usage/billing meters.
5. Deploy a preview first; record rollback, deletion and backup/restore steps before any production change.

### Cloud workflow
Use the vendor CLI/SDK and a non-production project first. Set environment-specific configuration explicitly and confirm account/billing status.

## Practical example
**Task:** Store a user's private notes and verify cross-user reads are denied by rules.

1. Create a disposable development project or local emulator and record the selected region, environment and current quota/billing settings.
2. Implement one minimal path using a test identity and a least-privilege rule; keep credentials in the vendor's secret mechanism.
3. Test both an allowed operation and an operation that must be denied, then inspect the actual stored resource and service logs.
4. Deploy a preview only after the test passes; document rollback, resource cleanup and backup/restore behavior.

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
Free tiers, quotas, regions and billing policies change. Confirm the current pricing page and project billing state; do not assume a service is free or unlimited.

## Official documentation
- [https://firebase.google.com/docs/firestore](https://firebase.google.com/docs/firestore)
- Confirm product-specific instructions, supported versions and availability at the vendor's official documentation before relying on them.

## Verification checklist
- [ ] The requested outcome and constraints are met without unrelated changes.
- [ ] The workflow's focused example/check completed and its output was inspected.
- [ ] Relevant error, permission, edge-case and compatibility paths were considered.
- [ ] No credentials or unlicensed assets were introduced; cost and authorization limits are understood.
- [ ] The result, tested environment and any unverified assumptions are reported clearly.

## Status
**Last reviewed:** 2026-11-25. Workflow guidance reviewed for this repository; recheck official documentation and service availability before production use.
