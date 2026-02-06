#!/usr/bin/env zsh
set -euo pipefail
export HUGO_ENV=development
# Serve site locally for development. Use host 0.0.0.0 to allow remote testing (containers). Port 1313 is default.
hugo server -s ./ -D --minify --disableFastRender --bind 0.0.0.0 --port 1313
