#!/bin/bash

# Script to convert external image URLs to local Hugo shortcode references
# This will help process more images locally

echo "Converting external image URLs to local shortcode references..."

# Find all markdown files with external shafiq.in image URLs
find content -name "*.md" -type f | while read file; do
    echo "Processing: $file"
    
    # Create a backup
    cp "$file" "$file.bak"
    
    # Replace external URLs with shortcode references
    sed -i '' 's|!\[\([^]]*\)\](https://www\.shafiq\.in/wp-content/uploads/\([^)]*\))|{{< optimizedImage src="wp-content/uploads/\2" alt="\1" >}}|g' "$file"
    
    # Check if any changes were made
    if ! diff -q "$file" "$file.bak" > /dev/null; then
        echo "  Updated: $file"
        rm "$file.bak"
    else
        echo "  No changes needed: $file"
        rm "$file.bak"
    fi
done

echo "Conversion complete!"
echo "Now run 'hugo serve' to see the processed images count increase."