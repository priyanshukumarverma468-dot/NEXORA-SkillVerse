<!-- Generated from skills/catalog.json. Edit the catalog and run scripts/generate_skills.py. -->
---
name: WebView application development
description: Embed trusted web content in a native Android shell with deliberate navigation, origin and bridge controls.
category: apk-development
last-reviewed: 2026-11-25
---

# WebView application development

## Description
Embed trusted web content in a native Android shell with deliberate navigation, origin and bridge controls.

## Purpose
Use this guide to carry out the task below in a reproducible, reviewable way. It is an agent instruction set, not a claim that the external product or service is free, available in every region, or unchanged.

## When to use
- The task is specifically about webview application development.
- The requested output can be validated against a concrete requirement and target environment.
- You are authorized to use the project, account, media, device or service involved.

## Requirements
- A clearly scoped task, success criteria, target platform and permitted inputs.
- Access to a suitable test project, fixture or copy of user data.
- Review current vendor/runtime requirements before relying on version-specific behavior.

## Supported tools
Android Studio, Android SDK command-line tools, Gradle wrapper, emulator and adb; optional web tooling depends on the selected wrapper/framework.

## Installation
Install Android Studio or the official Android command-line tools and accept only required SDK licenses. Use the repository Gradle wrapper (`./gradlew`) rather than a global Gradle when present. Emulator/device setup is optional for static checks but needed for runtime verification.

## Step-by-step workflow
1. Inspect `settings.gradle`, module build files, manifest, SDK versions and existing build tasks before changing the project.
2. Implement the smallest app change using existing architecture and platform guidance; keep credentials and signing files outside source control.
3. Run the relevant Gradle task through the wrapper, for example `./gradlew assembleDebug`, and preserve the first actionable build error.
4. Install the correct artifact on an emulator or authorized device with `adb install -r <path-to-apk>` and test the changed flow.
5. Verify package ID, permissions, min/target SDK behavior, output path and signing state for the intended distribution channel.

### Android workflow
Use Android Studio or the official command-line SDK, Gradle wrapper, emulator and adb. Prefer free Android tooling; match project requirements before installing anything.

## Practical example
**Task:** Load a locally hosted development page in a WebView and test external-link behavior.

1. Check the module's actual task names (`./gradlew tasks`) and run its focused test task before building.
2. Build the intended variant with the project wrapper, for example `./gradlew assembleDebug`; record the variant and artifact path.
3. Install that artifact using `adb install -r <path-to-apk>` on an emulator or authorized device and exercise the named user journey.
4. Verify the changed behavior plus relevant permission-denial, rotation/lifecycle or offline state; inspect Logcat if it fails.

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
Android Studio and the Android SDK are available without a paid subscription for typical development. Devices, third-party SDKs, app-store accounts, signing/hosting services and proprietary tools may cost money; verify current terms and distribution requirements.

## Official documentation
- [https://developer.android.com/develop/ui/views/layout/webapps/webview](https://developer.android.com/develop/ui/views/layout/webapps/webview)
- Confirm product-specific instructions, supported versions and availability at the vendor's official documentation before relying on them.

## Verification checklist
- [ ] The requested outcome and constraints are met without unrelated changes.
- [ ] The workflow's focused example/check completed and its output was inspected.
- [ ] Relevant error, permission, edge-case and compatibility paths were considered.
- [ ] No credentials or unlicensed assets were introduced; cost and authorization limits are understood.
- [ ] The result, tested environment and any unverified assumptions are reported clearly.

## Status
**Last reviewed:** 2026-11-25. Workflow guidance reviewed for this repository; recheck official documentation and service availability before production use.
