#!/usr/bin/env python3
"""
Script to automatically update categories for all Hugo blog posts.
Follows best practices by:
1. Using only available categories from the categories folder
2. Assigning one primary category per post
3. Using tags for nuanced classification
4. Maintaining consistent formatting
"""

import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Available categories
AVAILABLE_CATEGORIES = {
    "architecture",
    "art",
    "board-games",
    "book-binding",
    "children",
    "design",
    "development",
    "financial",
    "formula1",
    "health",
    "history",
    "home-automation",
    "humour",
    "jokes",
    "management",
    "parenting",
    "productivity",
    "quote",
    "relationships",
    "self-help",
    "travel",
    "writing",
}

# Tag to category mapping
TAG_TO_CATEGORY = {
    "devops": "development",
    "continuous-delivery": "development",
    "continuous-deployment": "development",
    "automation": "development",
    "docker": "development",
    "kubernetes": "development",
    "terraform": "development",
    "ansible": "development",
    "jenkins": "development",
    "git": "development",
    "linux": "development",
    "ubuntu": "development",
    "solaris": "development",
    "unix": "development",
    "bash": "development",
    "perl": "development",
    "python": "development",
    "php": "development",
    "ruby": "development",
    "javascript": "development",
    "golang": "development",
    "go": "development",
    "java": "development",
    "rust": "development",
    "c++": "development",
    "database": "development",
    "sql": "development",
    "mysql": "development",
    "postgresql": "development",
    "mongodb": "development",
    "aws": "development",
    "azure": "development",
    "gcp": "development",
    "cloud": "development",
    "security": "development",
    "ssl": "development",
    "encryption": "development",
    "drupal": "development",
    "wordpress": "development",
    "typo3": "development",
    "web": "development",
    "api": "development",
    "rest": "development",
    "enterprise-architecture": "architecture",
    "architecture-model": "architecture",
    "architecture": "architecture",
    "management": "management",
    "project-management": "management",
    "stakeholder": "management",
    "stakeholder-analysis": "management",
    "raci": "management",
    "scrum": "management",
    "agile": "management",
    "lean": "management",
    "waterfall": "management",
    "process": "management",
    "quality": "management",
    "requirements": "management",
    "business": "management",
    "startup": "management",
    "productivity": "productivity",
    "self-help": "self-help",
    "personal-development": "self-help",
    "motivation": "self-help",
    "stoicism": "self-help",
    "philosophy": "self-help",
    "design": "design",
    "ui": "design",
    "ux": "design",
    "css": "design",
    "html": "design",
    "art": "art",
    "graphics": "design",
    "web-design": "design",
    "theme": "design",
    "template": "design",
    "writing": "writing",
    "blog": "writing",
    "content": "writing",
    "documentation": "writing",
    "quote": "quote",
    "quotes": "quote",
    "travel": "travel",
    "goa": "travel",
    "trip": "travel",
    "journey": "travel",
    "relationships": "relationships",
    "family": "parenting",
    "parenting": "parenting",
    "children": "children",
    "toddlers": "children",
    "finance": "financial",
    "financial": "financial",
    "health": "health",
    "music": "art",
    "history": "history",
    "formula1": "formula1",
    "board-games": "board-games",
    "book-binding": "book-binding",
    "home-automation": "home-automation",
    "humour": "humour",
    "humor": "humour",
    "jokes": "jokes",
}

TITLE_KEYWORDS = {
    "development": [
        "code",
        "script",
        "python",
        "perl",
        "ruby",
        "php",
        "javascript",
        "linux",
        "ubuntu",
        "docker",
        "kubernetes",
        "git",
        "error",
        "fixed",
        "how to",
        "tutorial",
        "guide",
        "setup",
        "install",
    ],
    "management": [
        "project",
        "stakeholder",
        "team",
        "process",
        "scrum",
        "risk",
        "planning",
        "management",
        "proposal",
        "contract",
    ],
    "architecture": ["architecture", "design", "model", "framework"],
    "writing": ["blog", "article", "reflection"],
    "productivity": ["productivity", "workflow"],
    "quote": ["quote", "wisdom"],
    "travel": ["travel", "trip", "goa"],
    "design": ["design", "ui", "ux", "theme", "website"],
    "children": ["child", "toddler", "baby", "kids"],
}


class CategoryUpdater:
    def __init__(self, blog_dir: Path):
        self.blog_dir = blog_dir
        self.updates = []
        self.errors = []

    def read_file(self, filepath: Path) -> str:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    def write_file(self, filepath: Path, content: str):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    def extract_frontmatter(self, content: str) -> Tuple[Optional[str], Optional[str]]:
        """Extract frontmatter and body. Returns (frontmatter, body)."""
        match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
        if not match:
            return None, None
        return match.group(1), match.group(2)

    def parse_frontmatter(self, fm: str) -> Dict:
        """Parse YAML frontmatter."""
        result = {"title": "", "categories": [], "tags": []}

        # Title
        m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if m:
            result["title"] = m.group(1).strip().strip("\"'")

        # Categories - handle both formats
        m = re.search(r"^categories:\s*\n([\s\S]*?)(?=\n[a-z_]+:|$)", fm, re.MULTILINE)
        if m:
            cat_block = m.group(1)
            cats = re.findall(r"^\s*[-*]\s+(.+)$", cat_block, re.MULTILINE)
            result["categories"] = [c.strip() for c in cats]

        # Tags
        m = re.search(r"^tags:\s*\n([\s\S]*?)(?=\n[a-z_]+:|$)", fm, re.MULTILINE)
        if m:
            tag_block = m.group(1)
            tags = re.findall(r"^\s*[-*]\s+(.+)$", tag_block, re.MULTILINE)
            result["tags"] = [t.strip() for t in tags]

        return result

    def suggest_category(self, metadata: Dict) -> str:
        """Suggest category based on tags, then title."""
        tags = metadata.get("tags", [])
        title = metadata.get("title", "").lower()

        # Score categories from tags
        scores = defaultdict(int)
        for tag in tags:
            tag_lower = tag.lower()
            if tag_lower in TAG_TO_CATEGORY:
                scores[TAG_TO_CATEGORY[tag_lower]] += 2
            for key, cat in TAG_TO_CATEGORY.items():
                if key in tag_lower:
                    scores[cat] += 1

        if scores:
            return max(scores, key=scores.get)

        # Score by title keywords
        for cat, keywords in TITLE_KEYWORDS.items():
            for kw in keywords:
                if kw in title:
                    return cat

        return "development"

    def needs_update(self, categories: List[str]) -> bool:
        """Check if category update needed."""
        if not categories:
            return True
        for cat in categories:
            if cat.lower() not in AVAILABLE_CATEGORIES:
                return True
        if any(
            c.lower() in ["uncategorized", "uncategorised", "activities", "learning"]
            for c in categories
        ):
            return True
        return False

    def update_frontmatter(self, fm: str, new_cat: str) -> str:
        """Update frontmatter with new category."""
        # Remove existing categories
        fm = re.sub(r"^categories:\s*\n(?:\s+[-*]\s.+\n?)*", "", fm, flags=re.MULTILINE)

        # Find insertion point (after date or draft, before tags)
        for pattern in [r"^draft:", r"^date:", r"^author:"]:
            m = re.search(pattern, fm, re.MULTILINE)
            if m:
                # Find end of line
                end = fm.find("\n", m.end())
                if end != -1:
                    insert_pos = end + 1
                    fm = (
                        fm[:insert_pos]
                        + f"categories:\n  - {new_cat}\n"
                        + fm[insert_pos:]
                    )
                    return fm

        # Fallback: add before tags or at end
        m = re.search(r"^tags:", fm, re.MULTILINE)
        if m:
            fm = fm[: m.start()] + f"categories:\n  - {new_cat}\n" + fm[m.start() :]
            return fm

        # Add at end
        if not fm.endswith("\n"):
            fm += "\n"
        fm += f"categories:\n  - {new_cat}\n"
        return fm

    def process_file(self, filepath: Path) -> bool:
        """Process single markdown file."""
        try:
            content = self.read_file(filepath)
            fm_text, body = self.extract_frontmatter(content)

            if fm_text is None:
                return False

            metadata = self.parse_frontmatter(fm_text)

            if not self.needs_update(metadata["categories"]):
                return False

            new_cat = self.suggest_category(metadata)
            fm_new = self.update_frontmatter(fm_text, new_cat)
            new_content = f"---\n{fm_new}---\n{body}"

            self.write_file(filepath, new_content)

            self.updates.append(
                {
                    "file": str(filepath.relative_to(self.blog_dir)),
                    "title": metadata["title"][:60],
                    "new_category": new_cat,
                    "old_categories": metadata["categories"],
                    "tags": metadata["tags"],
                }
            )

            return True
        except Exception as e:
            self.errors.append({"file": str(filepath), "error": str(e)})
            return False

    def run(self):
        """Process all blog posts."""
        files = sorted(self.blog_dir.glob("*/**/*.md"))
        files = [f for f in files if f.name != "_index.md"]

        for i, f in enumerate(files, 1):
            print(f"[{i}/{len(files)}] {f.name[:50]:50}", end="", flush=True)
            if self.process_file(f):
                print(" ✓")
            else:
                print(" -")

    def summary(self):
        """Print summary."""
        print("\n" + "=" * 80)
        print("CATEGORY UPDATE COMPLETE")
        print("=" * 80)
        print(f"Updated: {len(self.updates)} posts")
        print(f"Errors: {len(self.errors)}")

        if self.updates:
            print("\nNew Category Distribution:")
            dist = defaultdict(int)
            for u in self.updates:
                dist[u["new_category"]] += 1
            for cat, cnt in sorted(dist.items(), key=lambda x: -x[1]):
                print(f"  {cat:20} {cnt:4}")


def main():
    blog_dir = Path("/Users/ssa/Documents/GitHub/www.shafiq.in/content/en/blog")

    if not blog_dir.exists():
        print(f"ERROR: {blog_dir} not found")
        sys.exit(1)

    print("Starting category updates...\n")
    updater = CategoryUpdater(blog_dir)
    updater.run()
    updater.summary()

    # Save report
    report = {
        "timestamp": datetime.now().isoformat(),
        "total_updated": len(updater.updates),
        "total_errors": len(updater.errors),
        "updates": updater.updates[:20],  # Sample
        "errors": updater.errors[:5],
    }

    report_path = blog_dir.parent.parent / "category-update-report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\n✓ Report: {report_path}")


if __name__ == "__main__":
    main()
