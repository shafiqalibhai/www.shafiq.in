#!/bin/bash

# Script to download the latest Hugo version from GitHub

# Set default version or get latest from GitHub
LATEST_HUGO_VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest | grep tag_name | cut -d '"' -f 4 | sed 's/v//')

# Check if version was retrieved
if [ -z "$LATEST_HUGO_VERSION" ]; then
    echo "Error: Could not fetch latest Hugo version"
    exit 1
fi

echo "Installing Hugo version: $LATEST_HUGO_VERSION"

# Set the download URL
HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${LATEST_HUGO_VERSION}/hugo_extended_${LATEST_HUGO_VERSION}_linux-amd64.deb"

# Download the Debian package
echo "Downloading Hugo..."
wget -O /tmp/hugo.deb "$HUGO_URL"

# Check if download was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to download Hugo"
    exit 1
fi

# Install Hugo
echo "Installing Hugo..."
sudo dpkg -i /tmp/hugo.deb

# Clean up
rm /tmp/hugo.deb

echo "Hugo ${LATEST_HUGO_VERSION} installed successfully!"
