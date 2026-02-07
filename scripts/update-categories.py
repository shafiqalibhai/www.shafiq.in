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

# Available categories from the categories folder
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

# Tag to category mapping (high confidence mappings)
TAG_TO_CATEGORY = {
    # Development & Engineering (highest priority due to volume)
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
    # Architecture
    "enterprise-architecture": "architecture",
    "architecture-model": "architecture",
    "architecture": "architecture",
    # Management & Organization
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
    # Productivity & Self-help
    "productivity": "productivity",
    "self-help": "self-help",
    "personal-development": "self-help",
    "motivation": "self-help",
    "stoicism": "self-help",
    "philosophy": "self-help",
    # Design & Art
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
    # Writing & Content
    "writing": "writing",
    "blog": "writing",
    "content": "writing",
    "documentation": "writing",
    # Quotes & Philosophy
    "quote": "quote",
    "quotes": "quote",
    # Travel
    "travel": "travel",
    "goa": "travel",
    "trip": "travel",
    "journey": "travel",
    # Family & Relationships
    "relationships": "relationships",
    "family": "parenting",
    "parenting": "parenting",
    "children": "children",
    "toddlers": "children",
    # Other
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

# Title keyword mappings (for posts without tags)
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
        "build",
        "deploy",
        "install",
        "configuration",
        "error",
        "fixed",
        "how to",
        "tutorial",
        "guide",
        "setup",
    ],
    "management": [
        "project",
        "stakeholder",
        "team",
        "process",
        "scrum",
        "agile",
        "risk",
        "requirement",
        "raci",
        "planning",
        "management",
        "proposal",
        "contract",
    ],
    "architecture": [
        "architecture",
        "design pattern",
        "model",
        "framework",
        "enterprise",
    ],
    "writing": ["blog", "article", "content", "post", "thoughts", "reflection", "memo"],
    "productivity": [
        "productivity",
        "workflow",
        "efficiency",
        "system",
        "productivity",
        "gtd",
    ],
    "quote": ["quote", "motto", "wisdom", "reflection"],
    "travel": ["travel", "journey", "trip", "goa", "destination"],
    "design": [
        "design",
        "ui",
        "ux",
        "theme",
        "css",
        "html",
        "graphics",
        "visual",
        "website",
    ],
    "children": ["child", "toddler", "baby", "kids", "children", "parenting"],
}


class CategoryUpdater:
    def __init__(self, blog_dir: Path):
        self.blog_dir = blog_dir
        self.updates_made = []
        self.skipped = []
        self.errors = []

    def extract_frontmatter_sections(self, content: str) -> Tuple[str, str, str]:
        """Extract frontmatter, content, and the --- separators."""
        match = re.match(r"^(---\n)(.*?)\n(---\n)(.*)", content, re.DOTALL)
        if not match:
            return None, None, None

        return match.group(2), match.group(4), match.group(3)

    def parse_frontmatter(self, fm_text: str) -> Dict:
        """Parse YAML frontmatter."""
        result = {"title": "", "categories": [], "tags": [], "raw": fm_text}

        # Extract title
        title_match = re.search(
            r'^title:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE
        )
        if title_match:
            result["title"] = title_match.group(1).strip().strip("\"'")

        # Extract categories
        cat_match = re.search(
            r"^categories:\s*\n((?:\s{2,}-\s.+(?:\n|$))*)", fm_text, re.MULTILINE
        )
        if cat_match:
            cat_text = cat_match.group(1)
            cats = re.findall(r"^\s{2,}-\s(.+)$", cat_text, re.MULTILINE)
            result["categories"] = [c.strip() for c in cats]

        # Extract tags
        tag_match = re.search(
            r"^tags:\s*\n((?:\s{2,}-\s.+(?:\n|$))*)", fm_text, re.MULTILINE
        )
        if tag_match:
            tag_text = tag_match.group(1)
            tags = re.findall(r"^\s{2,}-\s(.+)$", tag_text, re.MULTILINE)
            result["tags"] = [t.strip() for t in tags]

        return result

    def suggest_category(self, metadata: Dict) -> str:
        """
        Suggest best category based on:
        1. Tags (highest confidence)
        2. Title keywords (medium confidence)
        3. Default to development
        """
        tags = metadata.get("tags", [])
        title = metadata.get("title", "").lower()

        # Priority 1: Map tags to categories
        tag_scores = defaultdict(int)
        for tag in tags:
            tag_lower = tag.lower()
            if tag_lower in TAG_TO_CATEGORY:
                category = TAG_TO_CATEGORY[tag_lower]
                tag_scores[category] += 2  # Higher weight for direct tag matches

            # Also check for partial matches
            for key, val in TAG_TO_CATEGORY.items():
                if key in tag_lower:
                    tag_scores[val] += 1

        if tag_scores:
            best_cat = max(tag_scores, key=tag_scores.get)
            return best_cat

        # Priority 2: Check title keywords
        for category, keywords in TITLE_KEYWORDS.items():
            for keyword in keywords:
                if keyword in title:
                    return category

        # Priority 3: Check if title itself is a tag mapping key
        for key, val in TAG_TO_CATEGORY.items():
            if key in title:
                return val

        # Default fallback
        return "development"

    def needs_update(self, current_categories: List[str]) -> bool:
        """Check if a post needs category update."""
        if not current_categories:
            return True

        # Check if all categories are valid
        for cat in current_categories:
            if cat.lower() not in AVAILABLE_CATEGORIES:
                return True

        # Check for placeholder categories
        if any(
            c.lower() in ["uncategorized", "uncategorised", "activities", "learning"]
            for c in current_categories
        ):
            return True

        return False

    def build_new_frontmatter(self, fm_text: str, new_category: str) -> str:
        """Replace or add category in frontmatter."""
        # Remove existing categories section
        fm_text = re.sub(
            r"^categories:\s*\n(?:\s{2,}-\s.+\n?)*", "", fm_text, flags=re.MULTILINE
        )

        # Find a good place to insert categories (after title, before tags)
        # Look for tags line
        tags_match = re.search(r"^tags:", fm_text, re.MULTILINE)
        if tags_match:
            insert_pos = tags_match.start()
            categories_section = f"categories:\n  - {new_category}\n"
            fm_text = fm_text[:insert_pos] + categories_section + fm_text[insert_pos:]
        else:
            # If no tags, append before disableHLJS or at end
            hljs_match = re.search(r"^disableHLJS:", fm_text, re.MULTILINE)
            if hljs_match:
                insert_pos = hljs_match.start()
                categories_section = f"categories:\n  - {new_category}\n"
                fm_text = (
                    fm_text[:insert_pos] + categories_section + fm_text[insert_pos:]
                )
            else:
                # Append at the end
                if not fm_text.endswith("\n"):
                    fm_text += "\n"
                fm_text += f"categories:\n  - {new_category}\n"

        return fm_text

    def process_file(self, filepath: Path) -> bool:
        """Process a single markdown file."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract frontmatter
            fm_text, body, sep = self.extract_frontmatter_sections(content)
            if fm_text is None:
                self.skipped.append(str(filepath.relative_to(self.blog_dir)))
                return False

            # Parse frontmatter
            metadata = self.parse_frontmatter(fm_text)

            # Check if update is needed
            if not self.needs_update(metadata["categories"]):
                return False

            # Suggest new category
            new_category = self.suggest_category(metadata)

            # Build new frontmatter
            new_fm = self.build_new_frontmatter(fm_text, new_category)

            # Build new content
            new_content = f"---\n{new_fm}---\n{body}"

            # Write back
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

            self.updates_made.append(
                {
                    "file": str(filepath.relative_to(self.blog_dir)),
                    "title": metadata["title"],
                    "old_categories": metadata["categories"],
                    "new_category": new_category,
                    "tags": metadata["tags"],
                }
            )

            return True

        except Exception as e:
            self.errors.append(
                {"file": str(filepath.relative_to(self.blog_dir)), "error": str(e)}
            )
            return False

    def process_all_posts(self) -> None:
        """Process all blog posts."""
        md_files = sorted(self.blog_dir.glob("*/**/*.md"))

        # Exclude index files
        md_files = [f for f in md_files if f.name != "_index.md"]

        for i, filepath in enumerate(md_files, 1):
            print(
                f"[{i}/{len(md_files)}] Processing: {filepath.name}...",
                end="",
                flush=True,
            )
            if self.process_file(filepath):
                print(" ✓ UPDATED")
            else:
                print(" -")

    def print_summary(self) -> None:
        """Print summary of updates."""
        print("\n" + "=" * 80)
        print("CATEGORY UPDATE SUMMARY")
        print("=" * 80)
        print(
            f"\nTotal files processed: {len(self.updates_made) + len(self.skipped) + len(self.errors)}"
        )
        print(f"Files updated: {len(self.updates_made)}")
        print(f"Files skipped: {len(self.skipped)}")
        print(f"Errors: {len(self.errors)}")

        if self.updates_made:
            print("\n" + "-" * 80)
            print("Category Distribution (Updated Posts):")
            print("-" * 80)
            cat_dist = defaultdict(int)
            for update in self.updates_made:
                cat_dist[update["new_category"]] += 1

            for cat, count in sorted(cat_dist.items(), key=lambda x: -x[1]):
                print(f"  {cat:20} {count:3} posts")

        if self.errors:
            print("\n" + "-" * 80)
            print("Errors:")
            print("-" * 80)
            for err in self.errors[:10]:  # Show first 10 errors
                print(f"  {err['file']}: {err['error']}")

    def save_report(self, report_path: Path) -> None:
        """Save detailed report as JSON."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_updated": len(self.updates_made),
                "total_skipped": len(self.skipped),
                "total_errors": len(self.errors),
            },
            "updates": self.updates_made,
            "errors": self.errors,
        }

        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)

        print(f"\n✓ Report saved to: {report_path}")


def main():
    blog_dir = Path("/Users/ssa/Documents/GitHub/www.shafiq.in/content/en/blog")

    if not blog_dir.exists():
        print(f"ERROR: Blog directory not found: {blog_dir}")
        sys.exit(1)

    print("Starting category update for all blog posts...")
    print(f"Blog directory: {blog_dir}\n")

    updater = CategoryUpdater(blog_dir)
    updater.process_all_posts()
    updater.print_summary()

    # Save report
    report_path = Path(
        "/Users/ssa/Documents/GitHub/www.shafiq.in/category-update-report.json"
    )
    updater.save_report(report_path)


if __name__ == "__main__":
    main()
