# Shafiq's Digital Garden

Welcome to my personal website and digital garden. This is a Hugo-powered blog where I share my thoughts, experiences, and knowledge across various topics.

## Features

- 📝 **Blog Posts**: Collection of articles spanning from 2009 to present
- 🌍 **Multi-lingual**: Support for English and French content
- 🔍 **Search**: Built-in search functionality powered by FlexSearch
- 🌙 **Dark Mode**: Automatic dark/light theme switching based on system preference
- 📱 **Responsive**: Mobile-friendly design
- 🏷️ **Categories & Tags**: Organized content structure
- ⚡ **Fast**: Optimized build and minification

## Tech Stack

- **Hugo**: Static site generator (v0.155.2+)
- **Theme**: hugo-book
- **Hosting**: GitHub Pages
- **CI/CD**: GitHub Actions

## Quick Start

### Prerequisites

- Hugo extended version 0.155.2 or higher
- Dart Sass (optional, for custom styles)
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/shafiqalibhai/www.shafiq.in.git
cd www.shafiq.in
```

2. Install Hugo (if not already installed):
- **macOS**: `brew install hugo`
- **Linux**: Download from [Hugo releases](https://github.com/gohugoio/hugo/releases)
- **Windows**: Use scoop or chocolatey

3. Initialize git submodules (theme):
```bash
git submodule update --init --recursive
```

4. Start local development server:
```bash
hugo server -D
```

The site will be available at `http://localhost:1313`

### Building for Production

```bash
hugo --minify
```

The output will be in the `public/` directory.

## Content Management

### Creating a New Post

Use the provided script:
```bash
./new-post.sh "Your Post Title"
```

Or manually:
```bash
hugo new posts/YYYY-MM-DD-your-post-title.md
```

### Content Structure

```
content.en/          # English content
├── _index.md       # Homepage
├── posts/          # Blog posts
│   ├── 2024/
│   ├── 2023/
│   └── ...
├── docs/           # Static pages
└── about/          # About page

content.fr/          # French content (same structure)
```

### Frontmatter Example

```yaml
---
title: "Your Post Title"
date: 2024-01-01T00:00:00+00:00
draft: false
categories:
  - Development
tags:
  - hugo
  - web-dev
Description: "A brief description of your post"
---
```

## Translation

### New Post Translation

Run the translation script:
```bash
./translate_content_fr.sh
```

This will automatically translate English content to French using the configured translation service.

### Translation Notes

- Translated files maintain the same structure
- Frontmatter is preserved
- Images and other assets are shared

## Images

### Adding Images

Place images in appropriate folders:
```
static/
├── images/
│   ├── blog/
│   └── profile/
static/
└── favicon.svg
```

### Image Optimization

Run the EXIF stripper to remove sensitive metadata:
```bash
./strip-exif.sh
```

## Deployment

### Automated Deployment

This site uses GitHub Actions for automated deployment to GitHub Pages. Simply push to the `main` branch and the site will be automatically built and deployed.

### Manual Deployment

1. Build the site:
```bash
./build.sh
```

2. Deploy to GitHub Pages:
```bash
./push.sh
```

## Configuration

Main configuration files:
- `config/_default/config.yml` - Hugo configuration
- `config/_default/params.toml` - Theme parameters
- `config/_default/languages.toml` - Multi-language settings

## Customization

### Theme Customization

1. Copy theme files to edit:
   - Layouts: `layouts/`
   - Static assets: `static/`
   - Data: `data/`

2. Modify colors, fonts, and other styling in your custom CSS

### SEO

- robots.txt is automatically generated
- sitemap.xml is configured
- OpenGraph and Twitter cards are enabled
- Meta descriptions and keywords are configured

## Scripts

| Script | Description |
|--------|-------------|
| `build.sh` | Build the site for production |
| `serve.sh` | Start local development server |
| `new-post.sh` | Create a new blog post |
| `push.sh` | Deploy to GitHub Pages |
| `translate_content_fr.sh` | Translate content to French |
| `strip-exif.sh` | Remove EXIF data from images |
| `download-hugo.sh` | Download Hugo binary |

## Contributing

This is a personal blog, but feel free to:
- Report issues
- Suggest improvements
- Fork for your own use

## License

See [LICENSE](LICENSE) for details.

## Connect

- **Twitter**: [@shafiqalibhai](https://twitter.com/shafiqalibhai)
- **GitHub**: [shafiqalibhai](https://github.com/shafiqalibhai)
- **LinkedIn**: [shafiqalibhai](https://linkedin.com/in/deployview)

## Acknowledgments

- [Hugo](https://gohugo.io/) - Static site generator
- [hugo-book](https://github.com/alex-shpak/hugo-book) - Theme
- [GitHub Pages](https://pages.github.com/) - Hosting

# www.shafiq.in

## Quick Start (development)

Install Hugo extended (recommended) and Node (for dev tooling):

```bash
# macOS (Homebrew)
brew install hugo node
```

Serve locally:

```bash
make install
make serve
# or
zsh ./serve.sh
```

Build production:

```bash
make build
# or
zsh ./build.sh
```

Optimized images

Use the new shortcode in your content to generate responsive images with WebP/AVIF fallbacks:

```markdown
{{< optimizedImage src="images/posts/example.jpg" alt="Descriptive alt text" >}}
```