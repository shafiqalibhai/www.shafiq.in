#!/usr/bin/env python3
"""
Hugo Blog Tag Updater
Systematically updates tags for all blog posts based on content analysis.
Follows best practices: lowercase, semantic, concise tags.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

# Comprehensive tag taxonomy
TAG_TAXONOMY = {
    # Technical Tools & Frameworks
    "ansible": ["ansible", "provisioner", "automation"],
    "terraform": ["terraform", "iac"],
    "packer": ["packer"],
    "docker": ["docker", "container", "containerization"],
    "kubernetes": ["kubernetes", "k8s", "pods", "scheduling"],
    "git": ["git", "scm", "version control", "merge", "rebase"],
    "perl": ["perl", "script", "expect"],
    "php": ["php", "installation", "server setup"],
    "python": ["python"],
    "ruby": ["ruby", "gem"],
    "go": ["go", "golang"],
    "java": ["java"],
    "javascript": ["javascript", "npm", "node"],
    "solaris": ["solaris", "system administration"],
    "ubuntu": ["ubuntu", "debian", "linux", "installation"],
    "firefox": ["firefox", "browser"],
    "vlc": ["vlc", "media player"],
    "drupal": ["drupal", "solr", "search"],
    "typo3": ["typo3", "cms", "extension"],
    "wordpress": ["wordpress"],
    "opensuse": ["opensuse", "linux"],
    "sap": ["sap", "sales and distribution", "erp", "module"],
    "azure": ["azure", "vm", "extension", "cloud"],
    "juniper": ["juniper", "hardening"],
    "linux": ["linux", "cli", "command line", "distro", "os"],
    "macos": ["mac", "xcode", "xcrun"],
    "openssl": ["openssl", "certificate", "ssl", "tls", "security"],
    "ssl": ["ssl", "certificate", "https"],
    "http": ["http", "curl", "request"],
    "ssh": ["ssh", "sshpass", "remote access"],
    "proxmox": ["proxmox", "vm"],
    "psql": ["psql", "postgresql", "database"],
    "flex": ["flex", "bison", "compiler"],
    # DevOps & Operations
    "devops": ["devops", "ci/cd", "continuous integration", "continuous deployment"],
    "deployment": ["deployment", "release"],
    "build": ["build", "release engineering"],
    "jenkins": ["jenkins", "ci"],
    "puppet": ["puppet", "configuration management"],
    "saltstack": ["saltstack", "salt"],
    "monitoring": ["monitoring", "temperature", "system"],
    "docker": ["docker", "container"],
    # Software Engineering & Architecture
    "architecture": [
        "architecture",
        "enterprise architecture",
        "archimate",
        "ea",
        "design",
    ],
    "design": ["design", "pattern", "template"],
    "testing": ["testing", "test automation", "qa", "quality assurance"],
    "database": ["database", "integration", "schema"],
    "api": ["api", "rest"],
    "web-development": ["web", "website", "design", "css", "html"],
    "design-patterns": ["pattern", "architecture"],
    "integration": ["integration", "system integration"],
    "microservices": ["microservices"],
    # Project & Product Management
    "project-management": ["project management", "pm", "scrum", "agile", "planning"],
    "requirements": ["requirements", "specification", "analysis"],
    "stakeholder": ["stakeholder", "raci", "matrix"],
    "process": ["process", "workflow"],
    "scope": ["scope", "success criteria"],
    "risk": ["risk", "assessment", "mitigation"],
    "documentation": ["documentation", "proposal", "template"],
    # Business & Management
    "management": ["management", "leadership", "business"],
    "leadership": ["leadership", "management"],
    "communication": ["communication", "presentation"],
    "stakeholder-management": ["stakeholder"],
    "strategy": ["strategy", "planning"],
    "business-strategy": ["business", "strategy"],
    "product": ["product", "development"],
    "content-strategy": ["content strategy", "digital"],
    "digital": ["digital", "online"],
    "sales": ["sales", "distribution", "e-commerce", "shipping"],
    "finance": ["finance", "financial"],
    # Personal Development & Soft Skills
    "productivity": ["productivity", "efficiency", "time management"],
    "personal-development": ["personal development", "self-help", "growth"],
    "people-skills": ["people skills", "communication", "interpersonal"],
    "emotional-intelligence": ["emotional intelligence", "ei", "psychology"],
    "leadership-development": ["leadership", "professional development"],
    "assertiveness": ["assertiveness"],
    "conflict-resolution": ["conflict", "resolution"],
    "negotiation": ["negotiation"],
    "mindfulness": ["mindfulness", "awareness", "meditation"],
    "philosophy": ["philosophy", "philosophy", "stoicism", "ethics"],
    "life-lessons": ["lessons", "experience", "reflection"],
    "career": ["career", "professional", "work"],
    "learning": ["learning", "education", "knowledge"],
    "writing": ["writing", "blog"],
    "creativity": ["creativity", "creative"],
    "humor": ["humor", "funny", "joke"],
    # Lifestyle & Interests
    "travel": ["travel", "goa", "geography", "location"],
    "health": ["health", "fitness", "wellness", "medicine"],
    "relationships": ["relationships", "personal", "family"],
    "parenting": ["parenting", "family"],
    "hobby": ["hobby", "hobby", "leisure"],
    "music": ["music", "culture"],
    "art": ["art", "design", "visual"],
    "book-binding": ["binding", "craft"],
    "self-care": ["self-care", "wellness"],
    "religion": ["religion", "spirituality", "faith"],
    "quote": ["quote", "wisdom", "inspiration"],
    # Content Types & Formats
    "tutorial": ["tutorial", "howto", "guide", "install", "setup", "configure"],
    "how-to": ["howto", "how-to", "guide", "step-by-step"],
    "reference": ["reference", "documentation", "manual"],
    "troubleshooting": ["error", "fix", "solve", "troubleshoot", "issue", "bug"],
    "code-snippet": ["code", "example", "snippet"],
    "opinion": ["opinion", "thoughts", "perspective", "rant"],
    "template": ["template", "sample", "document"],
    "news": ["news", "announcement", "release"],
    "case-study": ["case study", "analysis"],
    "research": ["research", "analysis", "study"],
    "resource": ["resource", "tools", "utilities"],
    "list": ["list", "collection"],
    "review": ["review", "critique"],
    "inspiration": ["inspiration", "motivation"],
}

# Keywords to tag mapping for semantic analysis
KEYWORD_TO_TAG = {}
for tag, keywords in TAG_TAXONOMY.items():
    for keyword in keywords:
        if keyword not in KEYWORD_TO_TAG:
            KEYWORD_TO_TAG[keyword] = []
        KEYWORD_TO_TAG[keyword].append(tag)


def extract_frontmatter(content: str) -> Tuple[Dict, str]:
    """Extract YAML frontmatter from markdown file."""
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        return {}, content

    try:
        frontmatter = yaml.safe_load(match.group(1))
        body = match.group(2)
        return frontmatter, body
    except yaml.YAMLError:
        return {}, content


def analyze_content(
    title: str, body: str, existing_tags: List[str], category: str
) -> List[str]:
    """Analyze post content and suggest tags."""
    text = (title + " " + body[:500]).lower()  # First 500 chars for performance

    # If already has good tags, keep them
    if existing_tags:
        # Clean up and normalize existing tags
        existing_tags = [tag.lower().strip() for tag in existing_tags if tag]

        # Map to canonical tags
        mapped_tags = set()
        for existing_tag in existing_tags:
            found = False
            for canonical, keywords in TAG_TAXONOMY.items():
                if existing_tag in keywords or any(
                    existing_tag in kw for kw in keywords
                ):
                    mapped_tags.add(canonical)
                    found = True
                    break
            if not found:
                # Keep non-standard tags if they're specific
                if len(existing_tag) > 3 and existing_tag not in [
                    "ios",
                    "otc",
                    "oci",
                    "cse",
                ]:
                    mapped_tags.add(existing_tag)

        return list(mapped_tags)[:3]

    # Find relevant tags from content
    suggested_tags = set()

    # First, check for exact keyword matches
    for keyword, tags in KEYWORD_TO_TAG.items():
        if keyword in text:
            suggested_tags.update(tags)

    # Add category-based tag
    if category and category != "Uncategorized":
        category_lower = category.lower().replace(" ", "-")
        if category_lower in TAG_TAXONOMY:
            suggested_tags.add(category_lower)
        else:
            # Try to find related tags
            for tag, keywords in TAG_TAXONOMY.items():
                if category.lower() in keywords:
                    suggested_tags.add(tag)

    # Limit to top 3 most relevant
    return list(suggested_tags)[:3]


def process_file(filepath: Path) -> Tuple[bool, str]:
    """Process a single markdown file and update tags."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        frontmatter, body = extract_frontmatter(content)

        if not frontmatter:
            return False, "No frontmatter found"

        title = frontmatter.get("title", "")
        existing_tags = frontmatter.get("tags", [])
        category = (
            frontmatter.get("categories", [None])[0]
            if frontmatter.get("categories")
            else None
        )

        # Skip non-post files
        if not title:
            return False, "No title found"

        # Analyze and suggest tags
        new_tags = analyze_content(title, body, existing_tags, category)

        # Only update if tags changed or missing
        if not new_tags:
            return False, "No tags identified"

        # Update frontmatter
        frontmatter["tags"] = new_tags

        # Reconstruct file
        new_frontmatter = yaml.dump(
            frontmatter, default_flow_style=False, allow_unicode=True
        )
        new_content = f"---\n{new_frontmatter}---\n{body}"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        return True, f"Updated tags: {', '.join(new_tags)}"

    except Exception as e:
        return False, str(e)


def main():
    """Main function to process all blog posts."""
    blog_paths = [
        Path("/Users/ssa/Documents/GitHub/www.shafiq.in/content/en/blog"),
        Path("/Users/ssa/Documents/GitHub/www.shafiq.in/content/fr/blog"),
    ]

    stats = {
        "total": 0,
        "updated": 0,
        "failed": 0,
        "skipped": 0,
    }

    for blog_path in blog_paths:
        if not blog_path.exists():
            continue

        print(f"\n{'=' * 60}")
        print(f"Processing: {blog_path}")
        print(f"{'=' * 60}")

        md_files = sorted(blog_path.rglob("*.md"))
        md_files = [f for f in md_files if f.name != "_index.md"]  # Skip index files

        for filepath in md_files:
            stats["total"] += 1
            success, message = process_file(filepath)

            if success:
                stats["updated"] += 1
                print(f"✓ {filepath.relative_to(blog_path.parent.parent)}: {message}")
            elif (
                "No tags identified" in message
                or "No frontmatter" in message
                or "No title" in message
            ):
                stats["skipped"] += 1
            else:
                stats["failed"] += 1
                print(f"✗ {filepath.relative_to(blog_path.parent.parent)}: {message}")

    print(f"\n{'=' * 60}")
    print("Summary:")
    print(f"  Total files: {stats['total']}")
    print(f"  Updated: {stats['updated']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Failed: {stats['failed']}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
