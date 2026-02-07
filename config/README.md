# Hugo Configuration Structure

This document explains the configuration organization and best practices for this Hugo site.

## Configuration Hierarchy

Hugo loads configuration files in this order of precedence (later overrides earlier):

1. **`_default/`** - Base configuration applied to all environments
2. **`development/`** - Overrides for local development (`hugo server`)
3. **`production/`** - Overrides for production builds (`hugo`)

## Configuration Files

### Core Configuration Files in `_default/`

#### `config.yml`
Main site configuration including:
- Site metadata (baseURL, title, language)
- Build settings (caching, output formats)
- Content settings (pagination, minification)
- Menu structure

#### `params.yml` (if split)
Theme-specific parameters:
- Site description and keywords
- Theme colors and appearance
- Feature toggles (search, comments, dark mode)
- Widget configuration

#### `security.yml` (if split)
Security and privacy settings:
- HTTP security headers
- Content Security Policy
- Privacy settings for third-party services

#### `outputs.yml` (if split)
Output format configuration:
- HTML output
- JSON feed format
- RSS feeds
- Sitemaps

## Environment-Specific Overrides

### Development Environment (`hugo server -D`)
- **File**: `config/development/config.yml`
- **Purpose**: Optimized for local development
- **Key Settings**:
  - `buildDrafts: true` - Show draft posts
  - `buildFuture: true` - Show scheduled posts
  - `minify.minifyOutput: false` - Disable minification for debugging
  - `googleAnalytics: ""` - Disable analytics locally

### Production Environment (`hugo --environment production`)
- **File**: `config/production/config.yml`
- **Purpose**: Optimized for production deployment
- **Key Settings**:
  - `buildDrafts: false` - Hide drafts
  - `buildFuture: false` - Hide scheduled posts
  - `minify.minifyOutput: true` - Enable minification
  - Include analytics ID

## Building for Different Environments

### Local Development
```bash
hugo server -D
# or
make serve
```

### Production Build
```bash
hugo --environment production
# or
HUGO_ENVIRONMENT=production hugo
```

## Configuration Best Practices

### 1. **Environment Variables**
Use environment variables for sensitive or environment-specific values:

```bash
# Set Google Analytics ID
export HUGO_GOOGLEANALYTICS=G-XXXXXXXXXX

# Set environment
export HUGO_ENVIRONMENT=production
```

Access in config:
```yaml
googleAnalytics: {{ getenv "HUGO_GOOGLEANALYTICS" }}
```

### 2. **Security Configuration**
- Store API keys and tokens in environment variables, not in config files
- Use `security.funcs` to control which environment variables can be accessed
- Keep security headers in production config only

### 3. **Multi-Language Support**
The `languages` section in config supports multiple languages:
- **English**: `en` - Primary language
- **French**: `fr` - Secondary language

Each language has its own content directory and URL structure.

### 4. **Output Formats**
Define which formats are generated for different page types:
- **home**: HTML, JSON (for search), RSS
- **page**: HTML only
- **section**: HTML, RSS

### 5. **Minification**
Production config enables minification:
- CSS/JS minification reduces file size
- Disabled in development for easier debugging

### 6. **Markup Configuration**
Hugo uses Goldmark for Markdown rendering:
- Table of contents levels: 2-4
- Syntax highlighting: base16-snazzy theme
- Safe rendering (HTML allowed in markdown)

## Performance Tips

### Caching
Hugo caches processed resources:
- Use `resources.Match()` and `.Permalink` for stable URLs
- Cache-busting via URL hash happens automatically for assets

### Build Performance
- Use `hugo --gc` to garbage collect unused resources
- Use `hugo --minify` for production
- Use `make build` for optimized production builds

### Content Organization
- Use `mainSections` to specify which sections appear on homepage
- Use `pagerSize` to control pagination
- Use `related` config to efficiently find related content

## Adding New Configuration Sections

When adding new configuration:

1. **Decide**: Should it be in `_default/` (all environments) or specific environment?
2. **Add**: Create entry in appropriate config file or new module file
3. **Document**: Add comment explaining the setting
4. **Test**: Test in development, then production
5. **Commit**: Use descriptive commit messages

Example:
```yaml
# config/_default/config.yml
newFeature:
  enabled: true
  setting1: value1
  setting2: value2  # Explanation of what this does
```

## Troubleshooting Configuration Issues

### Config Not Loading
1. Check YAML syntax: `yamllint config/`
2. Verify file paths use forward slashes
3. Check Hugo version: `hugo version`

### Setting Not Applied
1. Check environment override is not conflicting
2. Verify YAML indentation (spaces, not tabs)
3. Clear Hugo cache: `rm -rf resources/`

### Analytics Not Working
1. Verify `googleAnalytics` ID is set
2. Check privacy settings are not disabling it
3. Verify tracking in browser DevTools

## References

- [Hugo Configuration Documentation](https://gohugo.io/getting-started/configuration/)
- [Hugo Security Policy](https://gohugo.io/about/security-policy/)
- [Book Theme Documentation](https://github.com/alex-shpak/hugo-book)
