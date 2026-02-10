#!/usr/bin/env python3
"""
Script to standardize blog post categories.
Follows Hugo best practices with lowercase, hyphenated category names.
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

# Define the canonical categories (lowercase with hyphens)
CANONICAL_CATEGORIES = {
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

# Mapping of non-standard categories to canonical ones
CATEGORY_MAP = {
    "Design": "design",
    "DESIGN": "design",
    "Development": "development",
    "DEVELOPMENT": "development",
    "Management": "management",
    "MANAGEMENT": "management",
    "Business": "management",
    "Goa": "travel",
    "uncategorised": "writing",
    "Uncategorised": "writing",
}


def extract_categories_from_fm(fm_text: str) -> List[str]:
    """Extract categories from YAML frontmatter text."""
    categories = []
    in_categories_block = False

    for line in fm_text.split("\n"):
        # Check if we're at the categories line
        if line.startswith("categories:"):
            in_categories_block = True
            # Check if there's a value on the same line
            match = re.search(r"categories:\s*\[(.*?)\]", line)
            if match:
                # Flow style array: categories: [cat1, cat2]
                cats_str = match.group(1)
                categories = [c.strip().strip("'\"") for c in cats_str.split(",")]
                in_categories_block = False
                break
            continue

        # If we're in categories block, collect items
        if in_categories_block:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if re.match(r"^\w+:", line):
                # We've hit another YAML key
                in_categories_block = False
                break
            if stripped.startswith("- "):
                # Array item
                cat = re.sub(r"^-\s+", "", stripped).strip().strip("'\"")
                if cat:
                    categories.append(cat)

    return categories


def normalize_categories(categories: List[str]) -> List[str]:
    """Normalize category names to canonical lowercase format."""
    if not categories:
        return ["writing"]  # Default category

    normalized = []
    for cat in categories:
        if isinstance(cat, str):
            cat = cat.strip()
            # Map non-standard to standard
            if cat in CATEGORY_MAP:
                normalized_cat = CATEGORY_MAP[cat]
            else:
                # Convert to lowercase and handle common variations
                normalized_cat = cat.lower().replace(" ", "-")

            # Only add if it's in our canonical set
            if normalized_cat in CANONICAL_CATEGORIES:
                if normalized_cat not in normalized:  # Avoid duplicates
                    normalized.append(normalized_cat)

    # If no valid categories, default to 'writing'
    if not normalized:
        normalized = ["writing"]

    return sorted(normalized)


def rebuild_categories_in_fm(fm_text: str, new_categories: List[str]) -> str:
    """Replace categories section in frontmatter with new values."""
    lines = fm_text.split("\n")
    result_lines = []
    skip_until_next_key = False

    for i, line in enumerate(lines):
        if line.startswith("categories:"):
            skip_until_next_key = True
            # Add new categories in list format
            result_lines.append("categories:")
            for cat in new_categories:
                result_lines.append(f"  - {cat}")
            continue

        # Skip old category items
        if skip_until_next_key:
            stripped = line.strip()
            # If this is a new YAML key, stop skipping
            if stripped and re.match(r"^\w+:", line):
                skip_until_next_key = False
                result_lines.append(line)
            elif stripped and not stripped.startswith("- "):
                # Non-list item after categories
                skip_until_next_key = False
                result_lines.append(line)
            # Otherwise skip this line (it's a category item)
        else:
            result_lines.append(line)

    return "\n".join(result_lines)


def is_empty_post(filepath: Path) -> bool:
    """Check if a post is empty (no meaningful content)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract content after frontmatter
        if content.startswith('---'):
            # Find the closing --- of frontmatter
            match = content.find('---\n', 3)
            if match != -1:
                # Get content after frontmatter
                content_after_fm = content[match+4:]
                # Remove frontmatter and check if content is empty
                content_after_fm = content_after_fm.strip()
                return len(content_after_fm) == 0
        
        # If no frontmatter or other issues, check entire content
        content = content.strip()
        return len(content) == 0
        
    except Exception as e:
        print(f"Error checking if post is empty: {e}")
        return False


def process_file(filepath: Path) -> Tuple[bool, str]:
    """
    Process a single markdown file to normalize categories.
    Returns (was_modified, message)
    """
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return False, f"Error reading: {e}"

    if not content.startswith("---"):
        # Check if this is an empty post
        if is_empty_post(filepath):
            try:
                filepath.unlink()
                return True, "Removed empty post"
            except Exception as e:
                return False, f"Error removing empty post: {e}"
        return False, "No frontmatter found"

    # Find the closing --- of frontmatter
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        # Check if this is an empty post
        if is_empty_post(filepath):
            try:
                filepath.unlink()
                return True, "Removed empty post"
            except Exception as e:
                return False, f"Error removing empty post: {e}"
        return False, "Could not parse frontmatter"

    fm_text = match.group(1)
    body = match.group(2)

    # Check if this is an empty post
    if is_empty_post(filepath):
        try:
            filepath.unlink()
            return True, "Removed empty post"
        except Exception as e:
            return False, f"Error removing empty post: {e}"

    # Extract current categories
    current_categories = extract_categories_from_fm(fm_text)
    if not current_categories:
        current_categories = []

    # Normalize
    normalized_categories = normalize_categories(current_categories)

    # Check if anything changed
    current_sorted = sorted(current_categories)
    normalized_sorted = sorted(normalized_categories)

    if current_sorted == normalized_sorted:
        return False, f"No changes: {normalized_categories}"

    # Rebuild frontmatter with new categories
    new_fm = rebuild_categories_in_fm(fm_text, normalized_categories)

    # Reconstruct file
    new_content = f"---\n{new_fm}\n---\n{body}"

    try:
        filepath.write_text(new_content, encoding="utf-8")
        old_str = ", ".join(current_categories) if current_categories else "(empty)"
        new_str = ", ".join(normalized_categories)
        return True, f"{old_str} → {new_str}"
    except Exception as e:
        return False, f"Error writing: {e}"


def main():
    """Main function to process all blog posts."""
    blog_dir = Path("/Users/ssa/Documents/GitHub/www.shafiq.in/content/en/blog")

    if not blog_dir.exists():
        print(f"Error: Blog directory not found: {blog_dir}")
        sys.exit(1)

    # Find all markdown files
    md_files = list(blog_dir.rglob("*.md"))

    # Filter out _index.md files
    md_files = [f for f in md_files if f.name != "_index.md"]

    print(f"Found {len(md_files)} markdown files to process\n")

    modified_count = 0
    failed_count = 0

    for filepath in sorted(md_files):
        was_modified, message = process_file(filepath)

        status = "✓" if was_modified else "·"
        relative_path = filepath.relative_to(blog_dir.parent.parent)
        print(f"{status} {relative_path}: {message}")

        if was_modified:
            modified_count += 1
        elif "Error" in message:
            failed_count += 1

    print(f"\n{'=' * 80}")
    print(
        f"Summary: {modified_count} files modified, {failed_count} errors, {len(md_files) - modified_count - failed_count} unchanged"
    )
    print(f"{'=' * 80}")


if __name__ == "__main__":
    main()
