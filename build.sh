#!/usr/bin/env zsh
set -euo pipefail
# Prefer bundled hugo-mobile if present (used historically), else use system hugo
DEST_DIR="../../www.shafiq.in-dist"
if [[ -x ./hugo-mobile ]]; then
  echo "Using ./hugo-mobile to build site -> $DEST_DIR"
  ./hugo-mobile --destination "$DEST_DIR" --minify --gc --enableGitInfo
else
  echo "Using system hugo to build site -> $DEST_DIR"
  hugo --minify --gc --enableGitInfo --destination "$DEST_DIR"
fi
