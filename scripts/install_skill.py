#!/usr/bin/env python3
"""Copy one skill to an agent's documented skill directory."""

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill", help="skill path relative to skills/, e.g. video-editing/ffmpeg")
    parser.add_argument("--destination", required=True, type=Path, help="agent's documented skills directory")
    parser.add_argument("--force", action="store_true", help="replace an existing destination SKILL.md")
    args = parser.parse_args()

    relative = Path(args.skill)
    if relative.is_absolute() or ".." in relative.parts or len(relative.parts) != 2:
        parser.error("skill must be a category/skill path beneath skills/")
    source = (SKILLS / relative / "SKILL.md").resolve()
    if not source.is_relative_to(SKILLS.resolve()) or not source.is_file():
        parser.error(f"unknown skill: {args.skill}")
    target = args.destination.expanduser() / relative.name / "SKILL.md"
    if target.exists() and not args.force:
        parser.error(f"{target} already exists; use --force to replace it")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    print(f"Installed {args.skill} to {target}")


if __name__ == "__main__":
    main()
