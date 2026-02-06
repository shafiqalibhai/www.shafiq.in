#!/usr/bin/env bash
set -euo pipefail
MODEL="qwen3:30b-a3b-instruct-2507-q4_K_M"
LOGFILE="translate_content_fr.log"

echo "Translation run started: $(date)" >> "$LOGFILE"

# Iterate all markdown files under content.fr (robust recursive traversal)
find content.fr/posts/2009 -type f -name '*.md' -print0 | while IFS= read -r -d '' f; do
  echo "\nProcessing: $f" | tee -a "$LOGFILE"

  # Extract frontmatter if present (find second '---' robustly)
  if awk 'NR==1 && /^---/{exit 0} END{exit 1}' "$f" >/dev/null 2>&1; then
    end_line=$(awk '/^---/{if(++c==2){print NR; exit}}' "$f" || true)
    if [ -z "$end_line" ]; then
      echo "Warning: unmatched frontmatter in $f, skipping" | tee -a "$LOGFILE"
      continue
    fi
    fm=$(sed -n "1,${end_line}p" "$f")
    body=$(sed -n "$((end_line+1)),\$p" "$f")
  else
    fm=""
    body=$(cat "$f")
  fi

  # Skip empty bodies
  if [ -z "$(echo "$body" | tr -d '[:space:]')" ]; then
    echo "Empty body for $f, skipping" | tee -a "$LOGFILE"
    continue
  fi

  prompt="Translate the following Markdown content from English to French. Preserve all Markdown structure and code blocks, and do NOT translate code blocks or frontmatter keys/values. Only translate visible text (titles, headings, paragraphs, lists, link text, image alt text). Do not add or remove sections. Return only the translated Markdown body (do NOT return frontmatter).\n\nCONTENT:\n$body"

  echo "Calling ollama model: $MODEL" | tee -a "$LOGFILE"

  # Retry loop
  translated=""
  max_retries=3
  for i in $(seq 1 $max_retries); do
    if translated=$(ollama run "$MODEL" "$prompt" 2>>"$LOGFILE"); then
      break
    else
      echo "Attempt $i failed for $f" | tee -a "$LOGFILE"
      sleep $((i * 2))
    fi
  done

  if [ -z "${translated:-}" ]; then
    echo "Translation empty for $f after $max_retries attempts; skipping" | tee -a "$LOGFILE"
    continue
  fi

  # Trim leading/trailing whitespace from model output
  translated=$(printf "%s" "$translated" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

  # Write translated content back, preserving frontmatter
  if [ -n "$fm" ]; then
    printf "%s\n%s\n" "$fm" "$translated" > "$f"
  else
    printf "%s\n" "$translated" > "$f"
  fi

  echo "Translated: $f" | tee -a "$LOGFILE"
  # brief pause to avoid overloading model
  sleep 1

done

echo "Translation run finished: $(date)" >> "$LOGFILE"
