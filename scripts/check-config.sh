#!/bin/bash
# ============================================================================
# Configuration Validation Script for Hugo Blog
# ============================================================================
# This script validates Hugo configuration files for common issues
# and best practices compliance.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "🔍 Hugo Configuration Validator"
echo "================================"
echo ""

# Check if Hugo is installed
if ! command -v hugo &> /dev/null; then
    echo "❌ Hugo is not installed"
    echo "   Install from: https://gohugo.io/installation/"
    exit 1
fi

HUGO_VERSION=$(hugo version | grep -oE "v[0-9]+\.[0-9]+\.[0-9]+")
echo "✓ Hugo found: $HUGO_VERSION"

# Check configuration files exist
echo ""
echo "📋 Checking configuration files..."

CONFIG_FILES=(
    "config/_default/config.yml"
    "config/development/config.yml"
    "config/production/config.yml"
)

MISSING=0
for config_file in "${CONFIG_FILES[@]}"; do
    if [ -f "$PROJECT_ROOT/$config_file" ]; then
        echo "✓ $config_file"
    else
        echo "❌ $config_file (MISSING)"
        MISSING=$((MISSING + 1))
    fi
done

if [ $MISSING -gt 0 ]; then
    echo "⚠️  $MISSING config files are missing"
fi

# Validate YAML syntax if yamllint is available
echo ""
echo "🎯 Validating YAML syntax..."

if command -v yamllint &> /dev/null; then
    if yamllint -c "{extends: relaxed, rules: {line-length: {max: 200}}}" \
        "$PROJECT_ROOT/config/_default/config.yml" \
        "$PROJECT_ROOT/config/development/config.yml" \
        "$PROJECT_ROOT/config/production/config.yml" 2>/dev/null; then
        echo "✓ YAML syntax is valid"
    else
        echo "⚠️  YAML validation warnings found (see above)"
    fi
else
    echo "ℹ️  yamllint not available (install: brew install yamllint)"
fi

# Run Hugo config validation
echo ""
echo "🔧 Running Hugo configuration check..."

if HUGO_ENVIRONMENT=development hugo config > /tmp/hugo_config_dev.json 2>&1; then
    echo "✓ Development configuration valid"
else
    echo "❌ Development configuration has errors:"
    cat /tmp/hugo_config_dev.json
    exit 1
fi

if HUGO_ENVIRONMENT=production hugo config > /tmp/hugo_config_prod.json 2>&1; then
    echo "✓ Production configuration valid"
else
    echo "❌ Production configuration has errors:"
    cat /tmp/hugo_config_prod.json
    exit 1
fi

# Check for common configuration issues
echo ""
echo "🚨 Checking for common issues..."

ISSUES=0

# Check baseURL
BASE_URL=$(grep "^baseURL:" "$PROJECT_ROOT/config/_default/config.yml" | head -1 | sed 's/.*: //' | tr -d '"' | tr -d "'")
if [ -z "$BASE_URL" ]; then
    echo "⚠️  baseURL not found in config"
    ISSUES=$((ISSUES + 1))
elif [ "$BASE_URL" = "http://localhost:1313/" ] || [ "$BASE_URL" = "http://example.org/" ]; then
    echo "⚠️  baseURL appears to be a default/placeholder value: $BASE_URL"
    ISSUES=$((ISSUES + 1))
else
    echo "✓ baseURL configured: $BASE_URL"
fi

# Check theme is set
if grep -q "^theme:" "$PROJECT_ROOT/config/_default/config.yml"; then
    THEME=$(grep "^theme:" "$PROJECT_ROOT/config/_default/config.yml" | sed 's/.*: //')
    if [ -d "$PROJECT_ROOT/themes/$THEME" ]; then
        echo "✓ Theme found: $THEME"
    else
        echo "⚠️  Theme directory not found: themes/$THEME"
        echo "   Run: git submodule update --init --recursive"
        ISSUES=$((ISSUES + 1))
    fi
fi

# Check languages are configured
if grep -q "^languages:" "$PROJECT_ROOT/config/_default/config.yml"; then
    LANG_COUNT=$(grep -A 10 "^languages:" "$PROJECT_ROOT/config/_default/config.yml" | grep "languageName:" | wc -l)
    echo "✓ Languages configured: $LANG_COUNT"
else
    echo "⚠️  Languages not configured"
    ISSUES=$((ISSUES + 1))
fi

# Check content directories exist
echo ""
echo "📁 Checking content directories..."

CONTENT_DIRS=(
    "content/en"
    "content/fr"
)

MISSING_DIRS=0
for dir in "${CONTENT_DIRS[@]}"; do
    if [ -d "$PROJECT_ROOT/$dir" ]; then
        COUNT=$(find "$PROJECT_ROOT/$dir" -name "*.md" 2>/dev/null | wc -l)
        echo "✓ $dir ($COUNT markdown files)"
    else
        echo "⚠️  $dir (directory not found)"
        MISSING_DIRS=$((MISSING_DIRS + 1))
    fi
done

# Summary
echo ""
echo "================================"
if [ $ISSUES -eq 0 ] && [ $MISSING_DIRS -eq 0 ]; then
    echo "✅ All checks passed!"
    echo ""
    echo "You can now build your site:"
    echo "  make serve     # Development server"
    echo "  make prod      # Production build"
    exit 0
else
    echo "⚠️  $ISSUES configuration issue(s) found"
    if [ $MISSING_DIRS -gt 0 ]; then
        echo "⚠️  $MISSING_DIRS missing content directory(ies)"
    fi
    echo ""
    exit 1
fi
