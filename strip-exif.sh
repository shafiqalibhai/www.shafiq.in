#!/usr/bin/env zsh
set -euo pipefail
# Strip EXIF metadata from images under static/ and resources/ (if any)
# Requires exiftool installed (brew install exiftool)
if ! command -v exiftool >/dev/null 2>&1; then
  echo "exiftool not found. Please install it (brew install exiftool)"
  exit 1
fi
# Process common image types
types=("jpg" "jpeg" "png")
for t in ${types[@]}; do
  echo "Processing *.$t files under static/"
  find static -type f -iname "*.$t" -print0 | xargs -0 -n1 -P4 exiftool -overwrite_original -all= || true
done

echo "Done. Consider running oxipng or cwebp for further optimization."
