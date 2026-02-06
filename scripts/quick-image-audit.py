#!/usr/bin/env python3
"""
Quick Image Audit for Hugo Blog - Simpler version focused on local validation
"""

import os
import re
from collections import defaultdict
from pathlib import Path


class SimpleImageAuditor:
    def __init__(self, repo_root=None):
        self.repo_root = Path(
            repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        self.content_dir = self.repo_root / "content"
        self.static_dir = self.repo_root / "static"

        self.issues = []
        self.external_images = []
        self.local_valid = []
        self.local_missing = []

    def extract_images(self, file_path):
        """Extract image references from markdown"""
        images = []
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Markdown images: ![alt](url)
            pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
            images.extend(re.findall(pattern, content))

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        return images

    def is_external(self, url):
        return url.startswith(("http://", "https://"))

    def check_local_file(self, img_path, file_dir):
        """Check if local file exists"""
        # Try relative path
        if img_path.startswith("/"):
            # Absolute path from repo
            paths_to_check = [
                self.repo_root / img_path.lstrip("/"),
                self.static_dir / img_path.lstrip("/"),
            ]
        else:
            # Relative path from markdown directory
            paths_to_check = [
                file_dir / img_path,
                (file_dir / img_path).resolve(),
                self.static_dir / img_path.lstrip("/"),
            ]

        for p in paths_to_check:
            if p.exists() and p.is_file():
                return True
        return False

    def audit(self):
        """Run audit"""
        md_files = list(self.content_dir.rglob("*.md"))

        print(f"🔍 Scanning {len(md_files)} markdown files...\n")

        for md_file in sorted(md_files):
            images = self.extract_images(md_file)
            if not images:
                continue

            rel_path = md_file.relative_to(self.repo_root)
            file_dir = md_file.parent

            for alt_text, img_url in images:
                if self.is_external(img_url):
                    self.external_images.append({"url": img_url, "file": str(rel_path)})
                else:
                    if self.check_local_file(img_url, file_dir):
                        self.local_valid.append(
                            {"path": img_url, "file": str(rel_path)}
                        )
                    else:
                        self.local_missing.append(
                            {
                                "path": img_url,
                                "file": str(rel_path),
                                "expected": str((file_dir / img_url).resolve()),
                            }
                        )

    def print_report(self):
        """Print summary report"""
        total = (
            len(self.external_images) + len(self.local_valid) + len(self.local_missing)
        )

        print("=" * 80)
        print("IMAGE AUDIT REPORT")
        print("=" * 80)
        print()

        print("📊 SUMMARY STATISTICS")
        print("-" * 80)
        print(f"Total image references: {total}")
        print(f"External images: {len(self.external_images)}")
        print(f"Local images found: {len(self.local_valid)}")
        print(f"Local images MISSING: {len(self.local_missing)}")
        print()

        if self.local_missing:
            print("⚠️  MISSING LOCAL IMAGES")
            print("-" * 80)
            for item in self.local_missing:
                print(f"\n📄 File: {item['file']}")
                print(f"   Image path: {item['path']}")
                print(f"   Expected at: {item['expected']}")
            print()

        if len(self.local_missing) == 0 and len(self.external_images) == 0:
            print("✅ STATUS: All local images are accessible!")
            print(
                "   External images: Validation skipped (would require network requests)"
            )
        elif len(self.local_missing) == 0:
            print("✅ STATUS: All local images are accessible!")
            print(f"   ({len(self.external_images)} external images not validated)")
        else:
            print(f"❌ STATUS: Found {len(self.local_missing)} missing local images")

        print()
        print("=" * 80)


def main():
    auditor = SimpleImageAuditor()
    auditor.audit()
    auditor.print_report()


if __name__ == "__main__":
    main()
