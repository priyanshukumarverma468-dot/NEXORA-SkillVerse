#!/usr/bin/env python3
"""Validate skill catalog output, required guide sections and repository-local links."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = (
    "Description", "Purpose", "When to use", "Requirements", "Supported tools",
    "Installation", "Step-by-step workflow", "Practical example", "Common errors",
    "Troubleshooting", "Security considerations", "Free and paid limitations",
    "Official documentation", "Verification checklist", "Status",
)
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def main():
    failures = []
    try:
        catalog = json.loads((ROOT / "skills/catalog.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Invalid skills catalog: {error}", file=sys.stderr)
        return 1

    listed = set()
    for category, entries in catalog.items():
        if not isinstance(entries, list) or not entries:
            failures.append(f"Empty or invalid catalog category: {category}")
            continue
        for entry in entries:
            if not isinstance(entry, list) or len(entry) != 4:
                failures.append(f"Invalid skill entry in {category}: {entry!r}")
                continue
            slug, _title, _purpose, _example = entry
            if slug in listed:
                failures.append(f"Duplicate skill slug: {slug}")
            listed.add(slug)
            path = ROOT / "skills" / category / slug / "SKILL.md"
            if not path.is_file():
                failures.append(f"Missing generated skill: {path.relative_to(ROOT)}")
    guides = sorted((ROOT / "skills").rglob("SKILL.md"))
    if len(guides) != len(listed) + 1:
        failures.append(f"Expected {len(listed) + 1} guides including OpenRouter; found {len(guides)}")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        if path in guides:
            for heading in REQUIRED_SECTIONS:
                if f"## {heading}" not in text:
                    failures.append(f"{path.relative_to(ROOT)} lacks section: {heading}")
            if text.count("```") % 2:
                failures.append(f"Unclosed fenced code block: {path.relative_to(ROOT)}")
            if "last-reviewed:" not in text:
                failures.append(f"Missing last-reviewed metadata: {path.relative_to(ROOT)}")
        for target in LINK.findall(text):
            target = target.split("#", 1)[0].strip()
            if not target:
                continue
            parsed = urlparse(target)
            if parsed.scheme in ("https", "http", "mailto"):
                if parsed.scheme in ("https", "http") and not parsed.netloc:
                    failures.append(f"Malformed external link in {path.relative_to(ROOT)}: {target}")
                continue
            if parsed.scheme:
                failures.append(f"Unsupported link scheme in {path.relative_to(ROOT)}: {target}")
                continue
            local = (path.parent / unquote(target)).resolve()
            if not local.is_relative_to(ROOT) or not local.exists():
                failures.append(f"Broken local link in {path.relative_to(ROOT)}: {target}")

    index = ROOT / "docs/SKILLS_INDEX.md"
    if not index.is_file():
        failures.append("Missing searchable skills index")
    else:
        index_text = index.read_text(encoding="utf-8")
        for category, entries in catalog.items():
            for slug, _title, _purpose, _example in entries:
                if f"../skills/{category}/{slug}/SKILL.md" not in index_text:
                    failures.append(f"Missing index entry for {category}/{slug}")
        if "../skills/ai-api-models/openrouter/SKILL.md" not in index_text:
            failures.append("Missing OpenRouter index entry")

    if failures:
        print("\n".join(f"ERROR: {message}" for message in failures), file=sys.stderr)
        return 1
    print(f"Validated {len(guides)} standalone skills across {len(catalog)} catalog categories and local links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
