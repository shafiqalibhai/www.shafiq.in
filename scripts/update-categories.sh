#!/bin/bash

# Blog post category updater script
# Updates all blog posts with appropriate categories following best practices

BLOG_DIR="/Users/ssa/Documents/GitHub/www.shafiq.in/content/en/blog"
BACKUP_DIR="/Users/ssa/Documents/GitHub/www.shafiq.in/.backup-categories-$(date +%Y%m%d-%H%M%S)"

# Create backup
echo "Creating backup of blog posts..."
mkdir -p "$BACKUP_DIR"
find "$BLOG_DIR" -name "*.md" -type f ! -name "_index.md" -exec cp -v {} "$BACKUP_DIR"/ \;

echo "Backup created at: $BACKUP_DIR"
echo ""
echo "Starting category updates..."

# Function to get suggested category based on file content
get_category() {
    local file="$1"
    local content=$(cat "$file")

    # Check tags for category hints
    if echo "$content" | grep -iq "tags:" | grep -iq "devops\|docker\|kubernetes\|git\|linux\|ubuntu\|code\|script\|python\|perl\|ruby\|php\|javascript\|error\|fixed"; then
        echo "development"
    elif echo "$content" | grep -iq "tags:" | grep -iq "project\|stakeholder\|management\|raci\|team\|scrum\|agile"; then
        echo "management"
    elif echo "$content" | grep -iq "tags:" | grep -iq "architecture\|enterprise"; then
        echo "architecture"
    elif echo "$content" | grep -iq "tags:" | grep -iq "design\|ui\|ux\|css\|html"; then
        echo "design"
    elif echo "$content" | grep -iq "tags:" | grep -iq "quote\|quotes"; then
        echo "quote"
    elif echo "$content" | grep -iq "tags:" | grep -iq "travel\|goa\|trip"; then
        echo "travel"
    elif echo "$content" | grep -iq "tags:" | grep -iq "writing\|blog\|article"; then
        echo "writing"
    elif echo "$content" | grep -iq "tags:" | grep -iq "children\|toddler"; then
        echo "children"
    elif echo "$content" | grep -iq "tags:" | grep -iq "productivity"; then
        echo "productivity"
    # Fallback to title keywords
    elif echo "$content" | grep -iq "title:.*code\|title:.*script\|title:.*how to\|title:.*tutorial\|title:.*install\|title:.*guide"; then
        echo "development"
    elif echo "$content" | grep -iq "title:.*project\|title:.*team\|title:.*management"; then
        echo "management"
    elif echo "$content" | grep -iq "title:.*architecture"; then
        echo "architecture"
    else
        echo "development"  # Default
    fi
}

# Process each markdown file
count=0
updated=0

for file in $(find "$BLOG_DIR" -name "*.md" -type f ! -name "_index.md" | sort); do
    count=$((count + 1))

    # Check if file has categories
    if grep -q "^categories:" "$file"; then
        # Check if it's an invalid category
        if grep "categories:" "$file" | grep -iq "uncategorized\|uncategorised\|activities\|learning"; then
            # Get suggested category
            suggested=$(get_category "$file")

            # Update the file
            # This is a simple approach - use sed to replace categories section
            sed -i '' "/^categories:/,/^[^ ]/{ /^categories:/d; /^  - /d; /^[^ ]/i\\
categories:\\
  - $suggested
}" "$file"

            updated=$((updated + 1))
            echo "✓ Updated: $(basename $file) -> $suggested"
        fi
    else
        # No categories found, add one
        suggested=$(get_category "$file")

        # Find the line number after date or author
        line_num=$(grep -n "^author:\|^date:" "$file" | tail -1 | cut -d: -f1)

        if [ ! -z "$line_num" ]; then
            # Insert after that line
            sed -i '' "${line_num}a\\
categories:\\
  - $suggested
" "$file"
        fi

        updated=$((updated + 1))
        echo "✓ Added: $(basename $file) -> $suggested"
    fi
done

echo ""
echo "=========================================="
echo "Category Update Summary"
echo "=========================================="
echo "Total files processed: $count"
echo "Files updated: $updated"
echo ""
echo "Backup available at: $BACKUP_DIR"
