#!/usr/bin/env python3
"""
Image Audit Tool for Hugo Blog
Checks if all images referenced in markdown files are valid and accessible
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import json
from collections import defaultdict
from datetime import datetime

class ImageAuditor:
    def __init__(self, repo_root=None):
        self.repo_root = Path(repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.content_dir = self.repo_root / "content"
        self.static_dir = self.repo_root / "static"

        self.results = {
            'total_images': 0,
            'external_images': [],
            'local_images': [],
            'missing_images': [],
            'invalid_urls': [],
            'by_file': defaultdict(list)
        }

    def extract_images_from_markdown(self, file_path):
        """Extract all image references from a markdown file"""
        images = []
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Match markdown image syntax: ![alt](url)
            pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
            matches = re.findall(pattern, content)

            # Also check for HTML img tags
            html_pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
            html_matches = re.findall(html_pattern, content)

            # Combine both
            for alt, url in matches:
                images.append(url)
            images.extend(html_matches)

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        return images

    def validate_external_url(self, url, timeout=5):
        """Check if external URL is accessible"""
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(req, timeout=timeout) as response:
                return response.status == 200
        except (HTTPError, URLError, Exception) as e:
            return False

    def validate_local_path(self, img_path, file_dir):
        """Check if local image file exists"""
        # Handle relative paths
        if img_path.startswith('/'):
            # Absolute path from repo root
            full_path = self.repo_root / img_path.lstrip('/')
        else:
            # Relative path from markdown file directory
            full_path = (file_dir / img_path).resolve()

        # Also check in static directory
        static_path = self.static_dir / img_path.lstrip('/')

        return full_path.exists() or static_path.exists()

    def is_external_url(self, url):
        """Check if URL is external"""
        return url.startswith(('http://', 'https://'))

    def audit(self):
        """Run the audit"""
        print(f"📊 Starting image audit...")
        print(f"Content directory: {self.content_dir}")
        print(f"Static directory: {self.static_dir}")
        print()

        # Find all markdown files
        md_files = list(self.content_dir.rglob('*.md'))
        print(f"Found {len(md_files)} markdown files")
        print()

        for md_file in md_files:
            images = self.extract_images_from_markdown(md_file)
            self.results['by_file'][str(md_file.relative_to(self.repo_root))] = images

            file_dir = md_file.parent

            for img in images:
                self.results['total_images'] += 1

                if self.is_external_url(img):
                    # Validate external URL
                    print(f"🌐 Checking external: {img[:60]}...")
                    if self.validate_external_url(img):
                        self.results['external_images'].append({
                            'url': img,
                            'file': str(md_file.relative_to(self.repo_root)),
                            'status': 'valid'
                        })
                        print(f"   ✓ Available")
                    else:
                        self.results['external_images'].append({
                            'url': img,
                            'file': str(md_file.relative_to(self.repo_root)),
                            'status': 'broken'
                        })
                        self.results['invalid_urls'].append({
                            'url': img,
                            'file': str(md_file.relative_to(self.repo_root)),
                            'type': 'external'
                        })
                        print(f"   ✗ Broken/Unreachable")
                else:
                    # Validate local file
                    print(f"📁 Checking local: {img}")
                    if self.validate_local_path(img, file_dir):
                        self.results['local_images'].append({
                            'path': img,
                            'file': str(md_file.relative_to(self.repo_root)),
                            'status': 'found'
                        })
                        print(f"   ✓ Found")
                    else:
                        self.results['local_images'].append({
                            'path': img,
                            'file': str(md_file.relative_to(self.repo_root)),
                            'status': 'missing'
                        })
                        self.results['missing_images'].append({
                            'path': img,
                            'file': str(md_file.relative_to(self.repo_root))
                        })
                        print(f"   ✗ Missing")

        print()

    def generate_report(self):
        """Generate markdown report"""
        report = []
        report.append("# Image Audit Report")
        report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Summary
        external_count = len(self.results['external_images'])
        local_count = len(self.results['local_images'])
        missing_count = len(self.results['missing_images'])
        invalid_count = len(self.results['invalid_urls'])

        report.append("## Summary Statistics")
        report.append(f"- **Total Image References**: {self.results['total_images']}")
        report.append(f"- **External Images**: {external_count}")
        report.append(f"- **Local Images**: {local_count}")
        report.append(f"- **Valid Images**: {self.results['total_images'] - missing_count - invalid_count}")
        report.append(f"- **Missing Local Images**: {missing_count}")
        report.append(f"- **Broken External Images**: {invalid_count}")
        report.append("")

        # Issues
        if missing_count > 0 or invalid_count > 0:
            report.append("## ⚠️ Issues Found\n")

            if missing_count > 0:
                report.append("### Missing Local Images\n")
                for item in self.results['missing_images']:
                    report.append(f"- **File**: {item['file']}")
                    report.append(f"  **Image**: {item['path']}\n")

            if invalid_count > 0:
                report.append("### Broken External Images\n")
                for item in self.results['invalid_urls']:
                    report.append(f"- **File**: {item['file']}")
                    report.append(f"  **URL**: {item['url']}\n")
        else:
            report.append("## ✅ Status\n")
            report.append("All images are accessible and valid!")
            report.append("")

        # Detailed breakdown by file
        if self.results['by_file']:
            report.append("\n## Detailed Breakdown by File\n")
            for file_path in sorted(self.results['by_file'].keys()):
                images = self.results['by_file'][file_path]
                if images:
                    report.append(f"### {file_path}")
                    report.append(f"Images: {len(images)}\n")
                    for img in images[:5]:  # Show first 5
                        report.append(f"- {img}")
                    if len(images) > 5:
                        report.append(f"- ... and {len(images) - 5} more\n")
                    report.append("")

        return "\n".join(report)

    def save_report(self, filename=None):
        """Save report to file"""
        if filename is None:
            filename = self.repo_root / "image-audit-report.md"

        report = self.generate_report()
        with open(filename, 'w') as f:
            f.write(report)

        return str(filename)

def main():
    auditor = ImageAuditor()
    auditor.audit()

    report_path = auditor.save_report()
    print(f"📄 Report saved to: {report_path}")
    print()

    # Print summary
    print(auditor.generate_report())

if __name__ == '__main__':
    main()
