HUGO=hugo
.PHONY: install serve build clean test
install:
	@echo "Install node dev dependencies if package.json exists"
	@if [ -f package.json ]; then npm ci; else echo "no package.json found"; fi
serve:
	$(HUGO) server -D --disableFastRender
build:
	hugo --minify --gc --enableGitInfo
clean:
	rm -rf public resources/_gen
test:
	@echo "Run Lighthouse CI locally (requires node and @lhci/cli)"
	@npx @lhci/cli autorun --config=.lighthouserc.json || true
