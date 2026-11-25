# NEXORA SkillVerse

**A practical, agent-readable library of task-specific AI and development skills.**

NEXORA SkillVerse provides reusable workflows for coding agents and human developers working on video, Android, AI applications, cloud services, programming, design, automation and testing. Every skill is a standalone `SKILL.md` with requirements, a workflow, a practical task, troubleshooting, safety guidance, official references and a verification checklist.

> Skills are instructions, not executable guarantees. Check current product documentation, permissions, regional availability and costs before acting. Model and cloud catalogs change.

## What is included

- **110 independent guides:** 109 task-specific guides plus a detailed OpenRouter integration guide. The searchable index is [docs/SKILLS_INDEX.md](docs/SKILLS_INDEX.md).
- **Portable format:** plain Markdown with `name` and `description` metadata; agents that do not load skills can use each guide as task context.
- **Runnable example:** a dependency-free OpenRouter client with explicit paid-model approval, catalog discovery, bounded fallback and focused tests.
- **Quality checks:** repository structure, required skill sections, local links and focused example tests run in GitHub Actions.
- **No repository subscription:** the library is free to browse and use. Third-party platforms, cloud resources, inference, SMS, hardware and software may have costs or license restrictions.

## Browse by category

| Category | Guides |
|---|---|
| [Video editing](skills/video-editing/) | Remotion, FFmpeg, CapCut, Alight Motion, stabilization, 4K, framing, captions, graphics, transitions, audio sync, background removal, compression, Shorts, Reels, thumbnails, quality analysis |
| [APK & Android development](skills/apk-development/) | App development/build/debug/analysis/optimization, WebView and web/React wrappers, project setup, manifest, permissions, icons, signing, compatibility, offline apps, UI |
| [AI development](skills/ai-development/) | Agents, autonomous coding, multi-agent design, workflows, prompts, AI apps/code/review/debugging/planning/memory/tools/browser/API integration |
| [AI API models](skills/ai-api-models/) | OpenRouter integration, live model discovery, explicit paid approval, fallback, error and usage handling |
| [Cloud](skills/cloud/) | Firebase Auth/Firestore/Hosting/Storage, Supabase database/Auth/Storage, Cloudflare Workers/Pages, sync and backup |
| [SMS](skills/sms/) | SMS API, OTP, phone verification, notifications, provider comparison |
| [Programming](skills/programming/) | HTML, CSS, JavaScript, TypeScript, React, Next.js, Python, Node.js, PHP, Java, Kotlin, SQL, REST, Git, GitHub, Actions |
| [Design](skills/designing/) | UI/UX, logos, app icons, websites, landing pages, dashboards, thumbnails, social assets, responsive design, design systems |
| [Automation](skills/automation/) | Browser automation, Playwright, Selenium, workflows, files, GitHub, builds, tests, APIs |
| [Testing & debugging](skills/testing/) | Reviews, bug detection, performance, security checks, APK/web/API/responsive/compatibility testing, logs, regression |

For exact names, links, and concise descriptions, use the [searchable skills index](docs/SKILLS_INDEX.md).

## Installation and use

### Use a guide directly
1. Browse the index and open the relevant `SKILL.md`.
2. Provide the complete guide to your AI agent, or follow it yourself.
3. Confirm the guide's prerequisites and authorization/cost limits before executing actions.
4. Run its verification checklist and report results, including checks not performed.

### Install into an agent's skill directory
The Markdown format is portable, but agent discovery paths and supported metadata differ. Check the current documentation for your agent, then copy one skill into its recognized skills directory. For example, where supported:

```sh
python scripts/install_skill.py video-editing/ffmpeg --destination .claude/skills
python scripts/install_skill.py ai-development/ai-tool-calling --destination .github/skills
```

The installer refuses to overwrite an existing destination unless `--force` is explicitly supplied. For any agent that does not support a skill directory, paste the guide into the task context or adapt its instructions to that agent's documented format. This repository does not claim that every agent auto-discovers the same format.

### Run the OpenRouter example
Python 3.10+; no third-party packages required:

```sh
python -m unittest examples.test_openrouter_client
python examples/openrouter_client.py --discover
```

To make an inference request, set `OPENROUTER_API_KEY` in a trusted server-side environment and pass a model ID copied from the live catalog:

```sh
export OPENROUTER_API_KEY='provided-by-your-secret-store'
python examples/openrouter_client.py --model 'provider/model-id-from-catalog' --prompt 'Use a non-sensitive test prompt'
```

The default allows only catalog entries with explicit zero pricing. Paid models require `--approve-paid-model 'exact/model-id'` for every approved paid candidate; pass it only after the user has approved the model and current price in an actual user-facing flow. The example is illustrative, not an approval interface or production spend limit. It returns token usage when provided and does not promise that free models are unlimited.

### Run repository checks
```sh
python scripts/generate_skills.py
python scripts/validate_repo.py
python -m unittest examples.test_openrouter_client
```

## Supported AI agents

The canonical skill format is standalone Markdown. It can be supplied as context to ChatGPT, Claude, Gemini, Cursor, VS Code agents and other tools that accept user-provided instructions. Native automatic discovery is agent-specific: see [docs/AGENT_COMPATIBILITY.md](docs/AGENT_COMPATIBILITY.md) and the target agent's current documentation. Do not assume identical frontmatter, paths, tool permissions or behavior.

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md). Catalog-generated pages are maintained in `skills/catalog.json`; OpenRouter has a hand-maintained guide and executable example. Skills should be specific, evidence-based, safe to execute and explicit about unverified claims.

## Security

Report vulnerabilities and sensitive exposures privately; see [SECURITY.md](SECURITY.md). Do not include real API keys, personal data or production credentials in examples or issues.

## License

Repository content is licensed under the [MIT License](LICENSE), except third-party names, products, trademarks, linked documentation and assets, which remain subject to their respective owners' terms. No third-party media assets are bundled.

## Roadmap

- Add reviewed, repeatable real-tool examples where licenses and test environments permit.
- Expand targeted test matrices for supported Android, browser, editor and cloud versions.
- Improve agent-specific adapters as their official skill formats stabilize.
- Refresh time-sensitive model, pricing, quota and platform guidance regularly.

## Limitations

This repository does not execute external workflows, provide API accounts, guarantee provider availability or deliver professional/legal/security certification. A skill's inclusion does not imply a tool was installed or an external integration was tested. Check each guide's status, current official documentation and verification results before production use.
