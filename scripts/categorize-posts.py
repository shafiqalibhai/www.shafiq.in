#!/usr/bin/env python3
"""
Script to analyze and suggest category updates for Hugo blog posts.
This script helps maintain consistent categorization following best practices.
"""

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

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

# Tag to category mapping (based on semantic similarity)
TAG_TO_CATEGORY = {
    # Development & Engineering
    "devops": "development",
    "development": "development",
    "programming": "development",
    "coding": "development",
    "javascript": "development",
    "python": "development",
    "perl": "development",
    "php": "development",
    "ruby": "development",
    "golang": "development",
    "go": "development",
    "docker": "development",
    "kubernetes": "development",
    "ci/cd": "development",
    "continuous-deployment": "development",
    "continuous-delivery": "development",
    "automation": "development",
    "jenkins": "development",
    "terraform": "development",
    "ansible": "development",
    "git": "development",
    "linux": "development",
    "ubuntu": "development",
    "solaris": "development",
    "unix": "development",
    "shell": "development",
    "bash": "development",
    "sed": "development",
    "awk": "development",
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
    "hardware": "development",
    "iot": "development",
    "web": "development",
    "api": "development",
    "rest": "development",
    "drupal": "development",
    "wordpress": "development",
    "typo3": "development",
    "java": "development",
    "rust": "development",
    "c++": "development",
    "architecture-model": "architecture",
    "enterprise-architecture": "architecture",
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
    # Productivity & Self-help
    "productivity": "productivity",
    "self-help": "self-help",
    "personal-development": "self-help",
    "motivation": "self-help",
    "stoicism": "self-help",
    "philosophy": "self-help",
    "best-practices": "development",
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
    "philosophy": "self-help",
    # Travel
    "travel": "travel",
    "goa": "travel",
    "trip": "travel",
    "journey": "travel",
    # Relationships & Social
    "relationships": "relationships",
    "family": "parenting",
    "parenting": "parenting",
    "children": "children",
    "personal": "relationships",
    # Other
    "business": "management",
    "startup": "management",
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
    "jokes": "jokes",
}


class PostCategorizer:
    def __init__(self, blog_content_dir: Path):
        self.blog_dir = blog_content_dir
        self.stats = defaultdict(int)
        self.posts = []

    def extract_frontmatter(self, file_path: Path) -> Dict:
        """Extract YAML frontmatter from a markdown file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Match frontmatter between --- delimiters
            match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
            if not match:
                return {}

            fm_text = match.group(1)
            frontmatter = {"_raw": fm_text}

            # Extract title
            title_match = re.search(
                r'title:\s*[\'"]?([^\'"]+)[\'"]?$', fm_text, re.MULTILINE
            )
            if title_match:
                frontmatter["title"] = title_match.group(1).strip()

            # Extract categories
            cat_match = re.search(r"categories:\s*\n((?:\s*-\s*.+\n?)*)", fm_text)
            if cat_match:
                cats = re.findall(r"^\s*-\s*(.+)$", cat_match.group(1), re.MULTILINE)
                frontmatter["categories"] = [c.strip() for c in cats]
            else:
                frontmatter["categories"] = []

            # Extract tags
            tag_match = re.search(r"tags:\s*\n((?:\s*-\s*.+\n?)*)", fm_text)
            if tag_match:
                tags = re.findall(r"^\s*-\s*(.+)$", tag_match.group(1), re.MULTILINE)
                frontmatter["tags"] = [t.strip() for t in tags]
            else:
                frontmatter["tags"] = []

            return frontmatter
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return {}

    def suggest_category(self, frontmatter: Dict) -> str:
        """Suggest a category based on title, tags, and current category."""
        tags = frontmatter.get("tags", [])
        current_cats = frontmatter.get("categories", [])
        title = frontmatter.get("title", "").lower()

        # Priority 1: If already has valid category, keep it
        for cat in current_cats:
            if cat.lower() in AVAILABLE_CATEGORIES:
                return cat.lower()

        # Priority 2: Check tags for category matches
        tag_scores = defaultdict(int)
        for tag in tags:
            tag_lower = tag.lower()
            if tag_lower in TAG_TO_CATEGORY:
                suggested = TAG_TO_CATEGORY[tag_lower]
                tag_scores[suggested] += 1
            # Check partial matches
            for key, val in TAG_TO_CATEGORY.items():
                if key in tag_lower or tag_lower in key:
                    tag_scores[val] += 0.5

        if tag_scores:
            best = max(tag_scores, key=tag_scores.get)
            return best

        # Priority 3: Keyword matching in title
        keywords = {
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
            ],
            "architecture": ["architecture", "design pattern", "model", "framework"],
            "writing": ["blog", "article", "content", "post", "thoughts", "reflection"],
            "productivity": [
                "productivity",
                "workflow",
                "efficiency",
                "system",
                "process",
                "getting things done",
            ],
            "quote": ["quote", '"', "motto"],
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
            ],
        }

        for category, keyword_list in keywords.items():
            for keyword in keyword_list:
                if keyword in title:
                    return category

        # Default fallback
        return "development"

    def categorize_posts(self) -> List[Dict]:
        """Process all blog posts and suggest categories."""
        results = []

        # Find all .md files in blog directory
        md_files = sorted(self.blog_dir.glob("*/**/*.md"))

        for filepath in md_files:
            if filepath.name == "_index.md":
                continue

            frontmatter = self.extract_frontmatter(filepath)
            if not frontmatter:
                continue

            suggested = self.suggest_category(frontmatter)
            current = frontmatter.get("categories", [])

            # Check if update needed
            needs_update = (
                not current
                or current[0].lower() not in AVAILABLE_CATEGORIES
                or current[0].lower() == "uncategorized"
            )

            results.append(
                {
                    "file": str(filepath.relative_to(self.blog_dir.parent.parent)),
                    "title": frontmatter.get("title", "N/A"),
                    "current": current,
                    "suggested": suggested,
                    "tags": frontmatter.get("tags", []),
                    "needs_update": needs_update,
                    "frontmatter": frontmatter,
                }
            )

        return results

    def print_summary(self, results: List[Dict]):
        """Print analysis summary."""
        print("\n" + "=" * 80)
        print("CATEGORY AUDIT SUMMARY")
        print("=" * 80)

        total = len(results)
        needs_update = sum(1 for r in results if r["needs_update"])

        print(f"\nTotal posts: {total}")
        print(f"Posts needing updates: {needs_update}")
        print(f"Posts with valid categories: {total - needs_update}")

        # Category distribution
        print("\n" + "-" * 80)
        print("Current Category Distribution:")
        print("-" * 80)
        cat_dist = defaultdict(int)
        for r in results:
            if r["current"]:
                cat_dist[r["current"][0]] += 1
            else:
                cat_dist["(no category)"] += 1

        for cat, count in sorted(cat_dist.items(), key=lambda x: -x[1]):
            print(f"  {cat:20} {count:3} posts")

        # Suggested category distribution
        print("\n" + "-" * 80)
        print("Suggested Category Distribution:")
        print("-" * 80)
        sugg_dist = defaultdict(int)
        for r in results:
            sugg_dist[r["suggested"]] += 1

        for cat, count in sorted(sugg_dist.items(), key=lambda x: -x[1]):
            print(f"  {cat:20} {count:3} posts")


def main():
    blog_dir = Path("/Users/ssa/Documents/GitHub/www.shafiq.in/content/en/blog")

    if not blog_dir.exists():
        print(f"Blog directory not found: {blog_dir}")
        sys.exit(1)

    categorizer = PostCategorizer(blog_dir)
    results = categorizer.categorize_posts()
    categorizer.print_summary(results)

    # Save detailed report
    report_file = Path(
        "/Users/ssa/Documents/GitHub/www.shafiq.in/category-audit-report.json"
    )
    with open(report_file, "w") as f:
        # Convert results to be JSON serializable
        json_results = []
        for r in results:
            json_results.append(
                {
                    "file": r["file"],
                    "title": r["title"],
                    "current": r["current"],
                    "suggested": r["suggested"],
                    "tags": r["tags"],
                    "needs_update": r["needs_update"],
                }
            )
        json.dump(json_results, f, indent=2)

    print(f"\n✓ Detailed report saved to: {report_file}")


if __name__ == "__main__":
    main()
