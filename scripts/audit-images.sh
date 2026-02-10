#!/bin/bash

# Image Audit Script
# This script checks if images referenced in markdown files are accessible
# and validates image links across blog posts, docs, and pages.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTENT_DIR="${REPO_ROOT}/content"
OUTPUT_FILE="${REPO_ROOT}/image-audit-report.md"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
TOTAL_IMAGES=0
BROKEN_IMAGES=0
EXTERNAL_IMAGES=0
LOCAL_IMAGES=0
LOCAL_MISSING=0
VALID_LOCAL=0

# Temporary files
TEMP_IMAGES=$(mktemp)
trap "rm -f ${TEMP_IMAGES}" EXIT

# Header
echo "# Image Audit Report" > "${OUTPUT_FILE}"
echo "" >> "${OUTPUT_FILE}"
echo "Generated on: $(date)" >> "${OUTPUT_FILE}"
echo "" >> "${OUTPUT_FILE}"

echo -e "${BLUE}Starting image audit...${NC}"
echo ""

# Extract all image references from markdown files
echo -e "${BLUE}Scanning markdown files for image references...${NC}"
find "${CONTENT_DIR}" -name "*.md" -type f | while read -r file; do
    # Extract image references using regex
    grep -oE '!\[[^\]]*\]\([^)]+\)' "$file" 2>/dev/null | sed 's/!\[\([^\]]*\)\](\([^)]*\))/\2/' | while read -r img_url; do
        if [ -n "$img_url" ]; then
            echo "${img_url}|${file}" >> "${TEMP_IMAGES}"
        fi
    done
done

# Process each unique image
echo -e "${BLUE}Validating image references...${NC}"
echo "" >> "${OUTPUT_FILE}"
echo "## Image Validation Results" >> "${OUTPUT_FILE}"
echo "" >> "${OUTPUT_FILE}"

while IFS='|' read -r img_url file; do
    TOTAL_IMAGES=$((TOTAL_IMAGES + 1))

    # Check if external URL
    if [[ $img_url =~ ^https?:// ]]; then
        EXTERNAL_IMAGES=$((EXTERNAL_IMAGES + 1))

        # Check if URL is accessible (with timeout)
        if timeout 5 curl -s -o /dev/null -w "%{http_code}" "$img_url" &>/dev/null | grep -q "^[23][0-9][0-9]$"; then
            STATUS="${GREEN}✓${NC} Available"
        else
            STATUS="${RED}✗${NC} Broken/Unreachable"
            BROKEN_IMAGES=$((BROKEN_IMAGES + 1))
            echo "- **Broken External Image**: ${img_url}" >> "${OUTPUT_FILE}"
            echo "  - File: ${file}" >> "${OUTPUT_FILE}"
        fi
        echo -e "${STATUS} - External: ${img_url}"
    else
        LOCAL_IMAGES=$((LOCAL_IMAGES + 1))

        # Resolve relative path
        DIR=$(dirname "$file")
        LOCAL_PATH="${DIR}/${img_url}"

        # Normalize path (remove ..)
        LOCAL_PATH=$(cd "$(dirname "$LOCAL_PATH")" 2>/dev/null && pwd)/$(basename "$LOCAL_PATH")

        if [ -f "$LOCAL_PATH" ]; then
            STATUS="${GREEN}✓${NC} Found"
            VALID_LOCAL=$((VALID_LOCAL + 1))
        else
            STATUS="${RED}✗${NC} Missing"
            LOCAL_MISSING=$((LOCAL_MISSING + 1))
            echo "- **Missing Local Image**: ${img_url}" >> "${OUTPUT_FILE}"
            echo "  - File: ${file}" >> "${OUTPUT_FILE}"
            echo "  - Expected path: ${LOCAL_PATH}" >> "${OUTPUT_FILE}"
        fi
        echo -e "${STATUS} - Local: ${img_url} (File: $(basename $file))"
    fi
done < "${TEMP_IMAGES}"

# Summary
echo "" >> "${OUTPUT_FILE}"
echo "## Summary" >> "${OUTPUT_FILE}"
echo "" >> "${OUTPUT_FILE}"
echo "- **Total Images**: ${TOTAL_IMAGES}" >> "${OUTPUT_FILE}"
echo "- **External Images**: ${EXTERNAL_IMAGES}" >> "${OUTPUT_FILE}"
echo "- **Local Images**: ${LOCAL_IMAGES}" >> "${OUTPUT_FILE}"
echo "- **Valid Local Images**: ${VALID_LOCAL}" >> "${OUTPUT_FILE}"
echo "- **Missing Local Images**: ${LOCAL_MISSING}" >> "${OUTPUT_FILE}"
echo "- **Broken/Unreachable External Images**: ${BROKEN_IMAGES}" >> "${OUTPUT_FILE}"
echo "" >> "${OUTPUT_FILE}"

if [ $BROKEN_IMAGES -eq 0 ] && [ $LOCAL_MISSING -eq 0 ]; then
    echo -e "${GREEN}✓ All images are accessible!${NC}"
    echo "✓ All images are accessible!" >> "${OUTPUT_FILE}"
else
    echo -e "${RED}✗ Found ${BROKEN_IMAGES} broken external images and ${LOCAL_MISSING} missing local images${NC}"
    echo "✗ Issues found - see details above" >> "${OUTPUT_FILE}"
fi

echo ""
echo -e "${BLUE}Audit report saved to: ${OUTPUT_FILE}${NC}"
