#!/bin/bash
# Script to delete TOML files after successful migration to YAML
# All TOML content has been merged into config.yml

cd "$(dirname "$0")/config/_default" || exit 1

echo "🗑️  Deleting TOML files from config/_default/..."
echo ""

# Delete each TOML file
files_deleted=0
for toml_file in hugo.toml params.toml markup.toml languages.toml menu.toml permalinks.toml relates.toml module.toml; do
    if [ -f "$toml_file" ]; then
        rm "$toml_file"
        echo "✅ Deleted: $toml_file"
        ((files_deleted++))
    fi
done

echo ""
echo "📊 Summary:"
echo "   Files deleted: $files_deleted"
echo ""
echo "✅ TOML cleanup complete!"
echo ""
echo "Remaining config files:"
ls -la *.yml 2>/dev/null || echo "No YAML files found"
echo ""
echo "📝 Note: All TOML content has been consolidated into config.yml"
