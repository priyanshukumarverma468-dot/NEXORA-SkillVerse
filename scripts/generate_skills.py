#!/usr/bin/env python3
"""Generate the standalone SKILL.md pages from skills/catalog.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "skills" / "catalog.json"
TODAY = "2026-11-25"

REFERENCE = {
    "video-editing": ("Media workflow", "Use a current, licensed editor or media tool suited to the requested transformation. Keep original media unchanged and work on a copy.", "https://ffmpeg.org/documentation.html"),
    "apk-development": ("Android workflow", "Use Android Studio or the official command-line SDK, Gradle wrapper, emulator and adb. Prefer free Android tooling; match project requirements before installing anything.", "https://developer.android.com/"),
    "ai-development": ("Agent workflow", "Use a supported runtime and a model/provider SDK only when required. Isolate credentials in environment variables or a secret manager.", "https://platform.openai.com/docs"),
    "cloud": ("Cloud workflow", "Use the vendor CLI/SDK and a non-production project first. Set environment-specific configuration explicitly and confirm account/billing status.", "https://firebase.google.com/docs"),
    "sms": ("Messaging workflow", "Use an account and sender approved for the target region. Store provider credentials server-side and use the provider's test mode where available.", "https://www.twilio.com/docs/sms"),
    "programming": ("Development workflow", "Use the repository's existing runtime, package manager, formatter and test runner. Install dependencies only when required and document required versions.", "https://developer.mozilla.org/"),
    "designing": ("Design workflow", "Use an appropriate design tool such as Figma, Penpot, Inkscape or a platform-native editor; verify the current license and export requirements.", "https://www.w3.org/WAI/standards-guidelines/"),
    "automation": ("Automation workflow", "Use a supported automation runtime and a test/staging target. Provide only the permissions needed for the defined task.", "https://playwright.dev/docs/intro"),
    "testing": ("Testing workflow", "Use the project's existing test and analysis tools. Run against controlled fixtures or staging data, not production unless explicitly authorized.", "https://testing.googleblog.com/"),
    "github": ("GitHub workflow", "Use Git and GitHub's documented web interface or CLI. Create a least-privilege token only if the task requires API access.", "https://docs.github.com/"),
}

TOOLS = {
    "video-editing": "FFmpeg/ffprobe for inspectable command-line transforms; Remotion for code-driven rendering; CapCut or Alight Motion for manual/mobile editing. Feature availability varies by platform and version.",
    "apk-development": "Android Studio, Android SDK command-line tools, Gradle wrapper, emulator and adb; optional web tooling depends on the selected wrapper/framework.",
    "ai-development": "A supported language runtime, provider API/SDK if needed, test framework, structured logging and secret store. Choose the simplest tool that meets the task.",
    "cloud": "Vendor CLI/console, SDK or REST API; local emulator/preview environment where provided; Git and a test identity.",
    "sms": "A regional SMS provider account/API, server-side runtime, queue/worker if asynchronous delivery is needed, and verified test recipient.",
    "programming": "The language runtime/compiler and formatter, linter and test runner already used by the repository.",
    "designing": "A vector/raster/prototyping tool appropriate to the output, plus target-device or browser previews.",
    "automation": "Playwright or Selenium for browser work; otherwise the narrowest vendor SDK/CLI and an isolated test target.",
    "testing": "The repository's test runner, static analysis and observability tools; device/browser matrix as applicable.",
    "github": "Git, GitHub CLI (`gh`) or GitHub web UI; Actions runner for workflow checks.",
}

INSTALL = {
    "video-editing": "Choose the official download or installation page for the selected editor. For FFmpeg, install a trusted distribution build and check `ffmpeg -version` and `ffprobe -version`. For Remotion, follow its current project setup guide and existing lockfile.",
    "apk-development": "Install Android Studio or the official Android command-line tools and accept only required SDK licenses. Use the repository Gradle wrapper (`./gradlew`) rather than a global Gradle when present. Emulator/device setup is optional for static checks but needed for runtime verification.",
    "ai-development": "Use the runtime's official installation method and the project's lockfile. Place provider keys in a local ignored environment file or managed secret store; never paste credentials into prompts, source, client bundles or logs.",
    "cloud": "Create or select a vendor account/project, install the vendor's official CLI/SDK only if needed, and configure a non-production project. Check current free-tier, quota, regional and billing settings before provisioning.",
    "sms": "Create a provider account and complete any identity/sender verification required in your target region. Review current per-message fees and test-mode restrictions before enabling sends.",
    "programming": "Use the project's declared version manager, package manifest and lockfile. If starting from scratch, follow the language or framework's official quickstart and pin a supported version.",
    "designing": "Install or use the official web/desktop editor and import only licensed assets. Set the target export size, color profile and platform constraints before production.",
    "automation": "Use the repository's pinned runtime and browser dependencies. Install Playwright/Selenium only when selected by the project; use a local test server or vendor sandbox before a live target.",
    "testing": "Use the project's existing test commands. Install additional tools only when the project already declares them or a concrete missing check requires them.",
    "github": "Install Git and optionally `gh` from their official distribution. Authenticate using the recommended browser/device flow; avoid storing broad-scope tokens in files.",
}

LIMITATIONS = {
    "video-editing": "FFmpeg is open-source software, but editor plans, export features, hardware, codecs and stock assets have separate terms. Check the selected build's license and current vendor plan; do not assume every app feature or asset is free.",
    "apk-development": "Android Studio and the Android SDK are available without a paid subscription for typical development. Devices, third-party SDKs, app-store accounts, signing/hosting services and proprietary tools may cost money; verify current terms and distribution requirements.",
    "ai-development": "Model inference, APIs, GPU compute and hosting may cost money and have quotas. Never assume a model/API is unlimited or free; obtain clear user approval before any paid inference and enforce a budget in the application.",
    "cloud": "Free tiers, quotas, regions and billing policies change. Confirm the current pricing page and project billing state; do not assume a service is free or unlimited.",
    "sms": "SMS is not universally free. Pricing, sender registration, verification, regional coverage and local regulations vary; obtain current provider terms and user consent.",
    "programming": "Many language toolchains are free/open source, but IDE features, commercial libraries, hosted services and deployment can cost money. Check each dependency's license and service plan before use.",
    "designing": "Free/open-source design tools exist, but premium editor features, fonts, stock imagery and icon packs may require payment or have usage restrictions. Check licenses and export limits for every asset.",
    "automation": "Automation frameworks may be free/open source, while hosted browsers, device farms, proxy services and target platforms can charge or restrict use. Confirm authorization, terms and current quotas.",
    "testing": "Local test tools may be free/open source, but hosted device/browser farms, commercial scanners and test data services can incur charges. Check license and service terms; test only authorized targets.",
    "github": "Git and public repository workflows are available without a repository subscription, but GitHub plan features, private runner minutes and external Actions/services have limits or costs. Check current plan and runner billing before enabling workflows.",
}

DOCS_BY_SLUG = {
    "remotion": "https://www.remotion.dev/docs",
    "ffmpeg": "https://ffmpeg.org/documentation.html",
    "capcut": "https://www.capcut.com/resource",
    "alight-motion": "https://alightmotion.com/",
    "android-apk-development": "https://developer.android.com/studio",
    "apk-building": "https://developer.android.com/build",
    "apk-debugging": "https://developer.android.com/studio/debug",
    "apk-analysis": "https://developer.android.com/tools/apkanalyzer",
    "apk-optimization": "https://developer.android.com/topic/performance",
    "webview-apps": "https://developer.android.com/develop/ui/views/layout/webapps/webview",
    "android-manifest": "https://developer.android.com/guide/topics/manifest/manifest-intro",
    "android-permissions": "https://developer.android.com/training/permissions",
    "app-icon-splash": "https://developer.android.com/develop/ui/views/launch/splash-screen",
    "apk-signing": "https://developer.android.com/studio/publish/app-signing",
    "android-build-errors": "https://developer.android.com/build",
    "android-compatibility": "https://developer.android.com/guide/practices/compatibility",
    "offline-android": "https://developer.android.com/topic/architecture/data-layer/offline-first",
    "android-ui": "https://developer.android.com/develop/ui",
    "firebase-authentication": "https://firebase.google.com/docs/auth",
    "firestore": "https://firebase.google.com/docs/firestore",
    "firebase-hosting": "https://firebase.google.com/docs/hosting",
    "firebase-storage": "https://firebase.google.com/docs/storage",
    "supabase-database": "https://supabase.com/docs/guides/database",
    "supabase-authentication": "https://supabase.com/docs/guides/auth",
    "supabase-storage": "https://supabase.com/docs/guides/storage",
    "cloudflare-workers": "https://developers.cloudflare.com/workers/",
    "cloudflare-pages": "https://developers.cloudflare.com/pages/",
    "html": "https://developer.mozilla.org/docs/Web/HTML",
    "css": "https://developer.mozilla.org/docs/Web/CSS",
    "javascript": "https://developer.mozilla.org/docs/Web/JavaScript",
    "typescript": "https://www.typescriptlang.org/docs/",
    "react": "https://react.dev/learn",
    "nextjs": "https://nextjs.org/docs",
    "python": "https://docs.python.org/3/",
    "nodejs": "https://nodejs.org/docs/latest/api/",
    "php": "https://www.php.net/manual/en/",
    "java": "https://docs.oracle.com/en/java/",
    "kotlin": "https://kotlinlang.org/docs/home.html",
    "sql": "https://www.postgresql.org/docs/current/",
    "rest-apis": "https://developer.mozilla.org/docs/Web/HTTP",
    "git": "https://git-scm.com/doc",
    "github": "https://docs.github.com/",
    "github-actions": "https://docs.github.com/actions",
    "playwright": "https://playwright.dev/docs/intro",
    "selenium": "https://www.selenium.dev/documentation/",
}

SPECIFIC = {
    "video-editing": [
        "Keep a read-only source and write outputs to a separate directory.",
        "Record source dimensions, frame rate, duration, audio tracks and color characteristics before choosing settings.",
        "Make the requested edit with the smallest set of transforms; do not silently crop, upscale, interpolate or alter color.",
        "Render a short sample around difficult motion, dialogue or transitions, then review it visually and with audio.",
        "Export to the requested aspect ratio, codec and delivery target; confirm the actual output rather than trusting export labels."
    ],
    "apk-development": [
        "Inspect `settings.gradle`, module build files, manifest, SDK versions and existing build tasks before changing the project.",
        "Implement the smallest app change using existing architecture and platform guidance; keep credentials and signing files outside source control.",
        "Run the relevant Gradle task through the wrapper, for example `./gradlew assembleDebug`, and preserve the first actionable build error.",
        "Install the correct artifact on an emulator or authorized device with `adb install -r <path-to-apk>` and test the changed flow.",
        "Verify package ID, permissions, min/target SDK behavior, output path and signing state for the intended distribution channel."
    ],
    "ai-development": [
        "Define the user goal, allowed data, model/tool boundaries, budget/latency constraints and a deterministic stop condition.",
        "Keep application policy and authorization in ordinary code; use schemas and runtime validation at every model/tool boundary.",
        "Implement a minimal end-to-end path with timeouts, bounded retries and redacted structured logs.",
        "Test normal, malformed, adversarial, timeout, provider-error and unauthorized-action cases with fixtures.",
        "Inspect the complete output/actions and require human approval where the workflow can change external or user data."
    ],
    "cloud": [
        "Confirm vendor, region, account, environment, service availability, current quotas and whether billing is enabled.",
        "Model identity, data access, retention and recovery before creating resources; use a disposable development project.",
        "Configure credentials through environment bindings/secret managers and implement the narrowest service policy.",
        "Test allowed and denied operations with separate test identities, then inspect logs and usage/billing meters.",
        "Deploy a preview first; record rollback, deletion and backup/restore steps before any production change."
    ],
    "sms": [
        "Confirm the recipient opted in, the use is lawful, and sender registration and delivery rules for the destination country.",
        "Keep provider API calls on a trusted server; never send API secrets to a browser or mobile application.",
        "Use cryptographically secure, short-lived, single-use codes when implementing OTP; store a keyed hash rather than a reusable plaintext code.",
        "Apply resend and verification limits per account, destination and network signal; avoid exposing whether an account/number exists.",
        "Test provider status callbacks, delayed/failed delivery and user opt-out; inspect actual provider charges before launch."
    ],
    "programming": [
        "Identify the actual runtime/compiler version, entry point, module system, conventions and existing tests before editing.",
        "Define input/output behavior and edge cases; use the language's native validation, error handling and type system.",
        "Make a minimal implementation that follows nearby patterns; do not introduce a dependency for functionality already available.",
        "Add a focused test for the requested behavior and at least one meaningful boundary/error case.",
        "Run the smallest relevant formatter, static check and test command; inspect the diff and report any unrun checks."
    ],
    "designing": [
        "Record audience, primary task, platform, dimensions, content constraints, brand rules and delivery formats.",
        "Map hierarchy and interaction states (including loading, empty, error, focus and disabled states where relevant).",
        "Build a responsive/accessibility-aware prototype using consistent spacing, typography, contrast and non-color cues.",
        "Review at real target sizes and with keyboard/assistive-technology considerations; get stakeholder approval for subjective choices.",
        "Export editable source plus named assets and document dimensions, fonts, colors, licensing and handoff assumptions."
    ],
    "automation": [
        "Confirm written authorization, the exact target/environment, allowed actions, rate limits and data handling rules.",
        "Prefer stable semantic locators/API contracts over coordinates or fragile DOM structure; never attempt access-control bypass.",
        "Use test identities and fixtures; add timeouts, idempotency safeguards, explicit retry conditions and a dry-run where feasible.",
        "Run a single bounded test, collect trace/log/screenshot evidence and verify resulting state before expanding the run.",
        "Require human confirmation before sending messages, publishing, purchases, account changes, deletes or other consequential actions."
    ],
    "testing": [
        "Translate the requirement into observable pass/fail criteria and identify the changed code paths and supported targets.",
        "Select representative fixtures and a controlled environment; protect production data and redact secrets/personal data.",
        "Reproduce failures with the narrowest check and save relevant command, environment and evidence.",
        "Confirm the root cause, add or update a regression test, and run targeted plus relevant compatibility/regression checks.",
        "Report actual results, skipped coverage, environment limits and remaining uncertainty without claiming unrun tests passed."
    ],
    "github": [
        "Confirm repository, branch, issue scope, project rules and required checks before making changes.",
        "Use a focused branch and small commits; review `git diff` and staged content before pushing or opening a pull request.",
        "Document setup, behavior changes, test commands, results and any migration/rollback notes for reviewers.",
        "Use minimal token/workflow permissions and treat fork pull-request content as untrusted.",
        "Wait for required checks and human review; merge or release only when explicitly authorized."
    ],
}

EXAMPLE_GUIDANCE = {
    "video-editing": [
        "Inspect the source with `ffprobe -v error -show_format -show_streams input.mp4` or the editor's media inspector; note tracks, duration, frame rate and dimensions.",
        "Duplicate the project/source and make only the requested edit; preserve the original frame and audio unless reframing or mixing is requested.",
        "Render a short sample containing the edit boundary, motion or dialogue; watch and listen at normal speed before rendering the complete output.",
        "Check the final file's actual dimensions, duration, audio tracks and playback; compare size and quality against the brief."
    ],
    "apk-development": [
        "Check the module's actual task names (`./gradlew tasks`) and run its focused test task before building.",
        "Build the intended variant with the project wrapper, for example `./gradlew assembleDebug`; record the variant and artifact path.",
        "Install that artifact using `adb install -r <path-to-apk>` on an emulator or authorized device and exercise the named user journey.",
        "Verify the changed behavior plus relevant permission-denial, rotation/lifecycle or offline state; inspect Logcat if it fails."
    ],
    "ai-development": [
        "Use a deterministic fake model/tool response first so the workflow can be tested without provider cost or network access.",
        "Validate model/tool input against an explicit schema and keep authorization checks in application code.",
        "Exercise the example with a valid request, malformed arguments, timeout and provider/tool error; assert the expected safe stop.",
        "Inspect the result and logs for unintended writes, secret disclosure, unbounded loops and unauthorized side effects."
    ],
    "cloud": [
        "Create a disposable development project or local emulator and record the selected region, environment and current quota/billing settings.",
        "Implement one minimal path using a test identity and a least-privilege rule; keep credentials in the vendor's secret mechanism.",
        "Test both an allowed operation and an operation that must be denied, then inspect the actual stored resource and service logs.",
        "Deploy a preview only after the test passes; document rollback, resource cleanup and backup/restore behavior."
    ],
    "sms": [
        "Use the provider's sandbox/test mode and a recipient that has explicitly consented; do not use a real OTP to test production access.",
        "Send one test request from a server-side process and retain the provider message ID/status without logging the secret or full phone number.",
        "Test invalid destination, opt-out, resend throttling, delayed status callback and duplicate job delivery.",
        "Review the provider's current destination-specific price and sender rules before enabling real traffic."
    ],
    "programming": [
        "Implement only the example task in the project's existing language version and module structure; validate untrusted input at the boundary.",
        "Add one success test and a boundary/error test using the current test framework; do not add a package just to demonstrate the feature.",
        "Run the existing formatter/linter and smallest relevant test command, then inspect the changed file and final diff.",
        "Compare actual behavior with the example's requirement and report commands, output and any unverified runtime assumptions."
    ],
    "designing": [
        "Create a small low-fidelity layout first, naming the target platform, dimensions, audience, primary action and asset rights.",
        "Produce the example as an editable component/frame; include focus, error, empty and disabled states where the interface needs them.",
        "Preview at the smallest target size and check contrast, keyboard order, text scaling and meaning that is not conveyed by color alone.",
        "Export an editable source and optimized deliverable; record size, color profile, font/asset licenses and handoff notes."
    ],
    "automation": [
        "Run against a local fixture or staging target with a test identity; verify the exact hostname and allowed actions first.",
        "Prefer role/label/API locators, set a bounded timeout and capture trace or sanitized logs on failure.",
        "Execute one dry-run or read-only test and verify the resulting state before allowing any write action.",
        "Test duplicate invocation, timeout and retry behavior; require human confirmation for external messages or irreversible changes."
    ],
    "testing": [
        "Turn the example into explicit pass/fail assertions and use a representative fixture that contains no production secrets or personal data.",
        "Run the narrowest test first and record the exact command, runtime/device/browser and failure evidence.",
        "After a fix, add a regression assertion that fails on the original defect and run related compatibility/smoke checks.",
        "Report the observed result, coverage not run, and any environmental limits; do not claim a check passed if it was not run."
    ],
    "github": [
        "Create a focused branch and inspect `git status --short` and `git diff --staged` before publishing changes.",
        "Use a test repository or pull request for the example; apply minimum workflow permissions and do not expose secrets to untrusted fork code.",
        "Run the repository's actual required checks and include their commands and results in the pull request description.",
        "Request review and wait for required checks; merge, publish or release only when explicitly authorized."
    ],
}

PROGRAMMING_EXAMPLES = {
    "html": "Use a `<form>` with an explicitly associated `<label for>` and `required` input; check keyboard focus and the browser's invalid-field behavior.",
    "css": "Use CSS Grid with `repeat(auto-fit, minmax(...))` or a project token-based breakpoint; verify no horizontal overflow at a narrow viewport.",
    "javascript": "Use `fetch` with an `AbortController`, check `response.ok`, and render distinct loading, success, error and timeout states.",
    "typescript": "Accept external JSON as `unknown` and narrow it with a runtime type guard before reading fields; test malformed data.",
    "react": "Keep the form value in component state, associate labels and errors accessibly, and disable duplicate submission while pending.",
    "nextjs": "Follow the installed Next.js version's routing conventions and keep secrets/data access on the server boundary, not in a client component.",
    "python": "Parse the sample CSV with `newline=''` and a context manager; test an empty file, malformed row and non-UTF-8 input policy.",
    "nodejs": "Validate request method/body size before processing; handle async errors and expose a health route without leaking environment secrets.",
    "php": "Validate request fields and use PDO prepared statements for SQL values; return a safe error response without echoing database details.",
    "java": "Define the method's null/empty/boundary behavior explicitly and cover those cases with the repository's existing test framework.",
    "kotlin": "Represent success/failure and nullable values explicitly; test coroutine cancellation and error outcomes if the method is suspending.",
    "sql": "Use bound parameters and an explicit transaction for the schema/data change; inspect the plan against representative, non-production data.",
    "rest-apis": "Use `curl -i` against the local endpoint with one valid and one invalid request; assert status code, response schema and authorization behavior.",
    "git": "Stage paths explicitly, inspect `git diff --cached`, then commit only the requested change; do not use a destructive reset to clean unrelated work.",
    "github": "Open a focused pull request with context, acceptance criteria, test evidence and links to the related issue; do not self-merge unless authorized.",
    "github-actions": "Use a pull-request workflow with `permissions: contents: read`, run checks without secrets, and test the YAML in a non-deployment workflow first."
}

def render(category, slug, title, purpose, example):
    family = category if category in SPECIFIC else "programming"
    reference_name, reference, docs = REFERENCE[family]
    paid_note = LIMITATIONS[family]
    docs = DOCS_BY_SLUG.get(slug, docs)
    workflow = SPECIFIC[family]
    tools = TOOLS[family]
    install = INSTALL[family]
    example_steps = list(EXAMPLE_GUIDANCE[family])
    if category == "programming":
        example_steps.insert(1, PROGRAMMING_EXAMPLES[slug])
    checks = [
        "The requested outcome and constraints are met without unrelated changes.",
        "The workflow's focused example/check completed and its output was inspected.",
        "Relevant error, permission, edge-case and compatibility paths were considered.",
        "No credentials or unlicensed assets were introduced; cost and authorization limits are understood.",
        "The result, tested environment and any unverified assumptions are reported clearly."
    ]
    return f"""<!-- Generated from skills/catalog.json. Edit the catalog and run scripts/generate_skills.py. -->
---
name: {title}
description: {purpose}
category: {category}
last-reviewed: {TODAY}
---

# {title}

## Description
{purpose}

## Purpose
Use this guide to carry out the task below in a reproducible, reviewable way. It is an agent instruction set, not a claim that the external product or service is free, available in every region, or unchanged.

## When to use
- The task is specifically about {title.lower()}.
- The requested output can be validated against a concrete requirement and target environment.
- You are authorized to use the project, account, media, device or service involved.

## Requirements
- A clearly scoped task, success criteria, target platform and permitted inputs.
- Access to a suitable test project, fixture or copy of user data.
- Review current vendor/runtime requirements before relying on version-specific behavior.

## Supported tools
{tools}

## Installation
{install}

## Step-by-step workflow
1. {workflow[0]}
2. {workflow[1]}
3. {workflow[2]}
4. {workflow[3]}
5. {workflow[4]}

### {reference_name}
{reference}

## Practical example
**Task:** {example}

{chr(10).join(f"{index}. {step}" for index, step in enumerate(example_steps, 1))}

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
{paid_note}

## Official documentation
- [{docs}]({docs})
- Confirm product-specific instructions, supported versions and availability at the vendor's official documentation before relying on them.

## Verification checklist
{chr(10).join("- [ ] " + item for item in checks)}

## Status
**Last reviewed:** {TODAY}. Workflow guidance reviewed for this repository; recheck official documentation and service availability before production use.
"""

def main():
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    count = 0
    index = ["# Skills index", "", "Browse or search this page to find a task-specific guide.", ""]
    for category, entries in catalog.items():
        index.extend([f"## {category.replace('-', ' ').title()}", ""])
        for slug, title, purpose, example in entries:
            path = ROOT / "skills" / category / slug / "SKILL.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render(category, slug, title, purpose, example), encoding="utf-8")
            index.append(f"- [{title}](../skills/{category}/{slug}/SKILL.md) — {purpose}")
            count += 1
        index.append("")
    index.extend(["## AI API models", "", "- [OpenRouter API integration and model routing](../skills/ai-api-models/openrouter/SKILL.md) — Discover models, gate paid use, route explicit fallbacks and track usage.", ""])
    (ROOT / "docs" / "SKILLS_INDEX.md").write_text("\n".join(index), encoding="utf-8")
    print(f"Generated {count} skill guides from {CATALOG.relative_to(ROOT)}.")

if __name__ == "__main__":
    main()
