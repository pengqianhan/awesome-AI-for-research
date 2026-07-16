#!/usr/bin/env python3
"""Add and refresh clickable GitHub star counts in the bilingual READMEs."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


README_PATHS = (Path("README.md"), Path("README_zh.md"))
STAR_RE = re.compile(
    r"(?<!`)<!--stars:(?P<repo>[^>]+)-->(?P<label>.*?)<!--/stars-->(?!`)",
    re.DOTALL,
)
GITHUB_LINK_RE = re.compile(
    r"\[(?P<label>[^\]]+)\]\((?P<url>https://github\.com/"
    r"(?P<owner>[^/\s)]+)/(?P<name>[^/\s)#?]+)(?:[^)]*)?)\)"
)
LIST_ITEM_RE = re.compile(r"^\d+\.\s+")
API_URL = "https://api.github.com/repos/{repo}"
TIMEOUT_SECONDS = 15
MAX_RETRIES = 3


def canonical_repo(owner: str, name: str) -> str:
    return f"{owner}/{name.removesuffix('.git')}"


def format_stars(count: int) -> str:
    if count >= 1_000_000:
        value = f"{count / 1_000_000:.1f}".removesuffix(".0")
        return f"{value}M"
    if count >= 1_000:
        value = f"{count / 1_000:.1f}".removesuffix(".0")
        return f"{value}k"
    return str(count)


def parse_existing_stars(label: str) -> str | None:
    match = re.search(r"⭐(?:&nbsp;|\s)*([\d.]+[kM]?)", label.strip())
    return match.group(1) if match else None


def build_marker(repo: str, stars: str) -> str:
    return f"<!--stars:{repo}-->⭐&nbsp;{stars}<!--/stars-->"


def add_missing_markers(text: str) -> tuple[str, int]:
    """Add linked markers after GitHub repository links in numbered entries."""
    added = 0
    updated_lines: list[str] = []

    for line in text.splitlines():
        if not LIST_ITEM_RE.match(line):
            updated_lines.append(line)
            continue

        repos_with_markers = {match.group("repo").strip().lower() for match in STAR_RE.finditer(line)}

        def replace(match: re.Match[str]) -> str:
            nonlocal added
            repo = canonical_repo(match.group("owner"), match.group("name"))
            if repo.lower() in repos_with_markers:
                return match.group(0)
            repos_with_markers.add(repo.lower())
            added += 1
            star_link = (
                f"[<!--stars:{repo}-->⭐&nbsp;updating<!--/stars-->]"
                f"(https://github.com/{repo})"
            )
            return f"{match.group(0)} {star_link}"

        updated_lines.append(GITHUB_LINK_RE.sub(replace, line))

    return "\n".join(updated_lines) + "\n", added


def fetch_stars(repo: str, token: str | None) -> tuple[int | None, int]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-ai-for-research-star-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(API_URL.format(repo=repo), headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            data = json.load(response)
            stars = data.get("stargazers_count")
            return (stars if isinstance(stars, int) else None), response.status
    except urllib.error.HTTPError as exc:
        return None, exc.code
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None, -1


def fetch_stars_with_retry(repo: str, token: str | None) -> int | None:
    for attempt in range(MAX_RETRIES):
        stars, status = fetch_stars(repo, token)
        if status == 200 and stars is not None:
            return stars
        if status in (401, 404) or attempt == MAX_RETRIES - 1:
            print(f"{repo}: failed (HTTP {status})", file=sys.stderr)
            return None
        wait_seconds = 2**attempt
        print(f"{repo}: retrying in {wait_seconds}s after HTTP {status}", file=sys.stderr)
        time.sleep(wait_seconds)
    return None


def refresh_markers(text: str, token: str | None, cache: dict[str, int | None]) -> tuple[str, int, int]:
    updated = 0
    unresolved = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal updated, unresolved
        repo = match.group("repo").strip()
        if repo not in cache:
            cache[repo] = fetch_stars_with_retry(repo, token)
        count = cache[repo]
        if count is None:
            if parse_existing_stars(match.group("label")) is None:
                unresolved += 1
            return match.group(0)
        replacement = build_marker(repo, format_stars(count))
        if replacement != match.group(0):
            updated += 1
        return replacement

    return STAR_RE.sub(replace, text), updated, unresolved


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--add-missing",
        action="store_true",
        help="Add linked star markers after unannotated GitHub repository links.",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Only add missing markers; do not call the GitHub API.",
    )
    args = parser.parse_args()

    missing = [str(path) for path in README_PATHS if not path.exists()]
    if missing:
        print(f"Missing README file(s): {', '.join(missing)}", file=sys.stderr)
        return 2

    token = os.environ.get("GITHUB_TOKEN")
    cache: dict[str, int | None] = {}
    total_unresolved = 0

    for path in README_PATHS:
        original = path.read_text(encoding="utf-8")
        text = original
        added = 0
        updated = 0
        unresolved = 0

        if args.add_missing:
            text, added = add_missing_markers(text)
        if not args.offline:
            text, updated, unresolved = refresh_markers(text, token, cache)

        if text != original:
            path.write_text(text, encoding="utf-8")
        print(f"{path}: {added} markers added, {updated} counts updated, {unresolved} unresolved")
        total_unresolved += unresolved

    return 1 if total_unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
