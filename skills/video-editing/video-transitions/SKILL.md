<!-- Generated from skills/catalog.json. Edit the catalog and run scripts/generate_skills.py. -->
---
name: Video transitions
description: Choose transitions that support continuity and rhythm; validate their timing at edit boundaries.
category: video-editing
last-reviewed: 2026-11-25
---

# Video transitions

## Description
Choose transitions that support continuity and rhythm; validate their timing at edit boundaries.

## Purpose
Use this guide to carry out the task below in a reproducible, reviewable way. It is an agent instruction set, not a claim that the external product or service is free, available in every region, or unchanged.

## When to use
- The task is specifically about video transitions.
- The requested output can be validated against a concrete requirement and target environment.
- You are authorized to use the project, account, media, device or service involved.

## Requirements
- A clearly scoped task, success criteria, target platform and permitted inputs.
- Access to a suitable test project, fixture or copy of user data.
- Review current vendor/runtime requirements before relying on version-specific behavior.

## Supported tools
FFmpeg/ffprobe for inspectable command-line transforms; Remotion for code-driven rendering; CapCut or Alight Motion for manual/mobile editing. Feature availability varies by platform and version.

## Installation
Choose the official download or installation page for the selected editor. For FFmpeg, install a trusted distribution build and check `ffmpeg -version` and `ffprobe -version`. For Remotion, follow its current project setup guide and existing lockfile.

## Step-by-step workflow
1. Keep a read-only source and write outputs to a separate directory.
2. Record source dimensions, frame rate, duration, audio tracks and color characteristics before choosing settings.
3. Make the requested edit with the smallest set of transforms; do not silently crop, upscale, interpolate or alter color.
4. Render a short sample around difficult motion, dialogue or transitions, then review it visually and with audio.
5. Export to the requested aspect ratio, codec and delivery target; confirm the actual output rather than trusting export labels.

### Media workflow
Use a current, licensed editor or media tool suited to the requested transformation. Keep original media unchanged and work on a copy.

## Practical example
**Task:** Create a short cross-dissolve between two shots without obscuring dialogue.

1. Inspect the source with `ffprobe -v error -show_format -show_streams input.mp4` or the editor's media inspector; note tracks, duration, frame rate and dimensions.
2. Duplicate the project/source and make only the requested edit; preserve the original frame and audio unless reframing or mixing is requested.
3. Render a short sample containing the edit boundary, motion or dialogue; watch and listen at normal speed before rendering the complete output.
4. Check the final file's actual dimensions, duration, audio tracks and playback; compare size and quality against the brief.

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
FFmpeg is open-source software, but editor plans, export features, hardware, codecs and stock assets have separate terms. Check the selected build's license and current vendor plan; do not assume every app feature or asset is free.

## Official documentation
- [https://ffmpeg.org/documentation.html](https://ffmpeg.org/documentation.html)
- Confirm product-specific instructions, supported versions and availability at the vendor's official documentation before relying on them.

## Verification checklist
- [ ] The requested outcome and constraints are met without unrelated changes.
- [ ] The workflow's focused example/check completed and its output was inspected.
- [ ] Relevant error, permission, edge-case and compatibility paths were considered.
- [ ] No credentials or unlicensed assets were introduced; cost and authorization limits are understood.
- [ ] The result, tested environment and any unverified assumptions are reported clearly.

## Status
**Last reviewed:** 2026-11-25. Workflow guidance reviewed for this repository; recheck official documentation and service availability before production use.
