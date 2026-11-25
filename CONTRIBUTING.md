# Contributing

Thanks for helping make NEXORA SkillVerse more useful and trustworthy.

## Add or update a skill

1. Search the [skills index](docs/SKILLS_INDEX.md) and catalog for an existing guide before creating a new one.
2. For catalog-managed guides, edit the relevant entry in `skills/catalog.json` and run `python scripts/generate_skills.py`. Avoid hand-editing generated skill pages.
3. For a genuinely tool-specific workflow that cannot fit the catalog template, add a standalone `skills/<category>/<slug>/SKILL.md` and explain its maintenance approach.
4. Use [templates/SKILL_TEMPLATE.md](templates/SKILL_TEMPLATE.md). Every guide needs task-specific requirements, supported tools, installation, ordered steps, practical example, common errors, troubleshooting, security, cost/availability limits, official documentation, verification checklist and a last-reviewed date.
5. Link official documentation, distinguish tested facts from assumptions, and do not claim a free service is unlimited. Never invent APIs, capabilities, prices or benchmark results.
6. Keep examples non-sensitive and authorized. Use placeholders for credentials. Do not automate destructive or consequential actions without confirmation and a recoverable plan.
7. Update the searchable index if you add a hand-maintained skill, then run:
   ```sh
   python scripts/generate_skills.py
   python scripts/validate_repo.py
   python -m unittest examples.test_openrouter_client
   ```
8. Describe actual test results and note which device, account, model, platform or service was not available to test.

## Pull requests

- Keep changes focused and review generated output in the diff.
- Explain the user problem, behavior change, and verification.
- Do not include credentials, user data, paid-service assumptions or unlicensed assets.
- Breaking changes to the skill format or generated catalog require a migration note.

## Reporting outdated information

Open an issue with the affected file, official reference, date checked and a minimal correction suggestion. Do not post secrets, phone numbers, private prompts or provider account details.
