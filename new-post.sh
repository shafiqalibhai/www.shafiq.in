#!/usr/bin/env bash
set -euo pipefail

# Prompt for title
read -rp "Post title: " TITLE
if [ -z "$TITLE" ]; then
  echo "Title required"
  exit 1
fi

# Slugify the title (lowercase, replace non-alphanum with -, trim)
SLUG=$(echo "$TITLE" | iconv -t ascii//TRANSLIT | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g' | sed -E 's/^-+|-+$//g')
YEAR=$(date +%Y)

EN_PATH="content/en/blog/$YEAR/$SLUG.md"
FR_PATH="content/fr/blog/$YEAR/$SLUG.md"

mkdir -p "$(dirname "$EN_PATH")" "$(dirname "$FR_PATH")"

hugo new "$EN_PATH"
hugo new "$FR_PATH"

echo "Created: $EN_PATH and $FR_PATH"
