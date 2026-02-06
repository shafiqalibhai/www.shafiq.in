#!/usr/bin/env bash
set -euo pipefail

MODEL="qwen3:30b-a3b-instruct-2507-q4_K_M"
DOCS_DIR="content/fr/docs"
LOGFILE="translate_docs_fr.log"
BACKUP_DIR="content/fr/docs.backup.$(date +%s)"

# Initialize log
echo "Translation run started: $(date)" > "$LOGFILE"
echo "Backing up original docs to: $BACKUP_DIR" | tee -a "$LOGFILE"
cp -r "$DOCS_DIR" "$BACKUP_DIR"

# Counter for stats
total_files=0
translated_files=0
skipped_files=0

# Iterate all markdown files under content/fr/docs (robust recursive traversal)
find "$DOCS_DIR" -type f -name '*.md' -print0 | while IFS= read -r -d '' f; do
  ((total_files++))
  echo -e "\n[$(date '+%H:%M:%S')] Processing: $f" | tee -a "$LOGFILE"

  # Check if file is empty
  if [ ! -s "$f" ]; then
    echo "File is empty, skipping" | tee -a "$LOGFILE"
    ((skipped_files++))
    continue
  fi

  # Extract frontmatter if present (find second '---' robustly)
  fm=""
  body=""

  if head -n 1 "$f" | grep -q "^---"; then
    # File starts with frontmatter marker
    end_line=$(awk '/^---/{if(++c==2){print NR; exit}}' "$f" || echo "")

    if [ -n "$end_line" ] && [ "$end_line" -gt 1 ]; then
      fm=$(sed -n "1,${end_line}p" "$f")
      body=$(sed -n "$((end_line+1)),\$p" "$f")
    else
      # Malformed frontmatter, treat entire file as body
      echo "Warning: malformed frontmatter, treating entire file as body" | tee -a "$LOGFILE"
      body=$(cat "$f")
    fi
  else
    # No frontmatter
    body=$(cat "$f")
  fi

  # Skip if body is empty or whitespace-only
  if [ -z "$(echo "$body" | tr -d '[:space:]')" ]; then
    echo "Body is empty, skipping" | tee -a "$LOGFILE"
    ((skipped_files++))
    continue
  fi

  # Create translation prompt
  prompt="Translate the following Markdown content from English to French. Preserve all Markdown structure, code blocks, tables, links, frontmatter, and special syntax like {{< shortcodes >}}, PlantUML diagrams, and mermaid charts.

IMPORTANT:
- Do NOT translate code blocks (Python, YAML, Terraform, Ansible, etc.)
- Do NOT translate URLs or link destinations
- Do NOT translate technical terms like 'Ansible', 'Terraform', 'Linux', 'Windows', 'PowerShell', etc.
- Preserve all spacing, indentation, and special characters
- Only translate visible human-readable text (titles, headings, paragraphs, list items, alt text)
- Return ONLY the translated Markdown body (do NOT return frontmatter)

CONTENT:
$body"

  echo "Calling ollama model: $MODEL" | tee -a "$LOGFILE"

  # Retry loop for robustness
  translated=""
  max_retries=3
  for attempt in $(seq 1 $max_retries); do
    if translated=$(ollama run "$MODEL" "$prompt" 2>>"$LOGFILE"); then
      break
    else
      echo "Attempt $attempt/$max_retries failed for $f" | tee -a "$LOGFILE"
      sleep $((attempt * 2))
    fi
  done

  if [ -z "${translated:-}" ]; then
    echo "ERROR: Translation empty after $max_retries attempts; skipping $f" | tee -a "$LOGFILE"
    ((skipped_files++))
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

  echo "✓ Translated: $f" | tee -a "$LOGFILE"
  ((translated_files++))

  # Brief pause to avoid overloading model
  sleep 1

done

echo -e "\n\n=== Translation Summary ===" | tee -a "$LOGFILE"
echo "Total files found: $total_files" | tee -a "$LOGFILE"
echo "Successfully translated: $translated_files" | tee -a "$LOGFILE"
echo "Skipped: $skipped_files" | tee -a "$LOGFILE"
echo "Backup location: $BACKUP_DIR" | tee -a "$LOGFILE"
echo "Translation run finished: $(date)" | tee -a "$LOGFILE"
