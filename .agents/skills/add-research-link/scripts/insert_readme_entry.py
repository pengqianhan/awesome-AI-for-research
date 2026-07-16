#!/usr/bin/env python3
"""Insert one bilingual awesome-list entry into README.md and README_zh.md."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


LIST_RE = re.compile(r"^(\d+)\.\s+")
HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$")
GITHUB_REPO_RE = re.compile(
    r"^https://github\.com/(?P<owner>[^/\s]+)/(?P<name>[^/\s#?]+)"
)


def clean(value: str) -> str:
    return " ".join(value.strip().split())


def github_star_link(url: str) -> str:
    match = GITHUB_REPO_RE.match(clean(url))
    if not match:
        return ""
    owner = match.group("owner")
    name = match.group("name").removesuffix(".git")
    repo = f"{owner}/{name}"
    return (
        f" [<!--stars:{repo}-->⭐&nbsp;updating<!--/stars-->]"
        f"(https://github.com/{repo})"
    )


def find_section(lines: list[str], title: str) -> tuple[int, int, int]:
    wanted = title.strip()
    start = -1
    level = 0

    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match and match.group(2).strip() == wanted:
            start = index
            level = len(match.group(1))
            break

    if start == -1:
        raise ValueError(f"section not found: {title}")

    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = HEADING_RE.match(lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break

    return start, end, level


def insert_entry(path: Path, section: str, name: str, url: str, desc: str, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    if url in text:
        return f"{path.name}: URL already present; skipped"

    lines = text.splitlines()
    start, end, _ = find_section(lines, section)
    last_item = -1
    last_number = 0

    for index in range(start + 1, end):
        match = LIST_RE.match(lines[index])
        if match:
            last_item = index
            last_number = int(match.group(1))

    cleaned_url = clean(url)
    entry = (
        f"{last_number + 1}. [{clean(name)}]({cleaned_url})"
        f"{github_star_link(cleaned_url)} - {clean(desc)}"
    )

    if last_item != -1:
        insert_at = last_item + 1
    else:
        insert_at = start + 1
        if insert_at < len(lines) and lines[insert_at].strip() == "":
            insert_at += 1

    new_lines = lines[:insert_at] + [entry] + lines[insert_at:]
    if not dry_run:
        path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    return f"{path.name}: inserted under '{section}' as item {last_number + 1}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme-en", default="README.md")
    parser.add_argument("--readme-zh", default="README_zh.md")
    parser.add_argument("--section-en", required=True)
    parser.add_argument("--section-zh", required=True)
    parser.add_argument("--name-en", required=True)
    parser.add_argument("--name-zh", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--desc-en", required=True)
    parser.add_argument("--desc-zh", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    readme_en = Path(args.readme_en)
    readme_zh = Path(args.readme_zh)

    missing = [str(path) for path in (readme_en, readme_zh) if not path.exists()]
    if missing:
        print(f"Missing README file(s): {', '.join(missing)}", file=sys.stderr)
        return 2

    try:
        messages = [
            insert_entry(
                readme_en,
                args.section_en,
                args.name_en,
                args.url,
                args.desc_en,
                args.dry_run,
            ),
            insert_entry(
                readme_zh,
                args.section_zh,
                args.name_zh,
                args.url,
                args.desc_zh,
                args.dry_run,
            ),
        ]
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    for message in messages:
        print(message)
    if args.dry_run:
        print("dry-run: no files changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
