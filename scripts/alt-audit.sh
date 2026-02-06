#!/usr/bin/env zsh
# Quick audit for image tags missing alt in generated public/ HTML or layouts
set -euo pipefail
echo "Searching for <img> tags without alt attribute in layouts and public..."
# Search layout templates
grep -R --line-number --include="*.html" "<img [^>]*alt=\"\"" layouts || true
# Search generated public HTML if exists
if [ -d public ]; then
  grep -R --line-number "<img [^>]*alt=\"\"" public || true
fi

echo "Done."
