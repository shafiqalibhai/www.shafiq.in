.PHONY: help install serve dev prod build clean test lint check-config

HUGO := hugo
ENVIRONMENT ?= development

help:
	@echo "Shafiq's Blog - Hugo Makefile Commands"
	@echo ""
	@echo "Development:"
	@echo "  make install        Install dependencies"
	@echo "  make serve          Start dev server with drafts/future posts"
	@echo "  make dev            Explicit development build (same as serve)"
	@echo ""
	@echo "Production:"
	@echo "  make prod           Build production version (minified, optimized)"
	@echo "  make build          Alias for prod"
	@echo ""
	@echo "Testing & Quality:"
	@echo "  make test           Run Lighthouse CI tests"
	@echo "  make check-config   Validate configuration"
	@echo "  make lint           Run linters (if available)"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean          Remove build artifacts and cache"
	@echo ""

install:
	@echo "Installing dependencies..."
	@if [ -f package.json ]; then npm ci; else echo "No package.json found"; fi
	@echo "✓ Dependencies installed"

serve: dev

dev:
	@echo "Starting development server..."
	@echo "Environment: development"
	@echo "Features: Drafts enabled, Future posts visible, Minification disabled"
	@echo ""
	$(HUGO) server -D --disableFastRender --environment development -M --ignoreCache --gc

prod: clean
	@echo "Building production site..."
	@echo "Environment: production"
	@echo "Features: Minified, optimized, analytics enabled"
	@echo ""
	HUGO_ENVIRONMENT=production $(HUGO) --minify --gc --enableGitInfo
	@echo "✓ Production build complete"
	@du -sh public/

build: prod

check-config:
	@echo "Checking Hugo configuration..."
	$(HUGO) config
	@echo "✓ Configuration valid"

lint:
	@echo "Running linters..."
	@if command -v yamllint >/dev/null 2>&1; then \
		echo "Checking YAML configuration files..."; \
		yamllint -c .yamllint config/ || true; \
	else \
		echo "yamllint not installed. Install with: brew install yamllint"; \
	fi

clean:
	@echo "Cleaning build artifacts..."
	rm -rf public resources/_gen
	rm -rf .hugo_build.lock
	@echo "✓ Cleaned"

test:
	@echo "Running tests..."
	@echo "1. Building site locally (production environment)..."
	$(MAKE) prod > /dev/null
	@echo "2. Running Lighthouse CI (requires node and @lhci/cli)..."
	@if [ -f .lighthouserc.json ]; then \
		npx @lhci/cli autorun --config=.lighthouserc.json || true; \
	else \
		echo "No .lighthouserc.json found"; \
	fi

# Advanced targets

server-prod:
	@echo "Starting production-like server (minified, no drafts)..."
	HUGO_ENVIRONMENT=production $(HUGO) server

reset:
	@echo "Resetting all caches and builds..."
	$(MAKE) clean
	rm -rf node_modules
	@echo "✓ Reset complete. Run 'make install' to reinstall."
