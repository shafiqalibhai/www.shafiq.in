#!/usr/bin/env python3
"""
Scan existing content/en/blog and content/fr/blog markdown files and add a `slug` front matter if missing.
This helps migrate timestamp-based filenames to explicit SEO-friendly slugs used by the site.

Usage: python3 scripts/slugify_posts.py [--dry-run]
"""

import argparse
import os
import re
import sys
from pathlib import Path

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def slugify(text: str) -> str:
    text = text.strip().lower()
    # Basic ascii transliteration fallback
    try:
        import unicodedata

        text = (
            unicodedata.normalize("NFKD", text)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    except Exception:
        pass
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text


def process_file(path: Path, dry_run: bool = False) -> bool:
    content = path.read_text(encoding="utf-8")
    m = FRONT_MATTER_RE.match(content)
    if not m:
        print(f"No front matter in {path}")
        return False
    fm = m.group(1)
    if re.search(r"^slug:\s*", fm, re.M):
        return False

    # Derive slug from title if present, otherwise from filename
    title_m = re.search(r"^title:\s*(?:\"|')?(.*?)(?:\"|'|$)", fm, re.M)
    if title_m:
        title = title_m.group(1).strip()
        derived = slugify(title)
    else:
        derived = slugify(path.stem)

    new_fm = fm + f'\nslug: "{derived}"\n'
    new_content = "---\n" + new_fm + "---\n" + content[m.end() :]

    if dry_run:
        print(f"Would add slug: {derived} to {path}")
    else:
        path.write_text(new_content, encoding="utf-8")
        print(f"Added slug: {derived} to {path}")
    return True


def find_blog_paths(root: Path):
    for lang in ("en", "fr"):
        base = root / "content" / lang / "blog"
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            yield p


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    changed = 0
    for p in find_blog_paths(repo_root):
        if process_file(p, dry_run=args.dry_run):
            changed += 1
    print(f"Processed {changed} files")


if __name__ == "__main__":
    main()
