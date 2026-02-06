#!/bin/bash

# Script to download the latest Hugo version from GitHub for macOS M1

# Set default version or get latest from GitHub
LATEST_HUGO_VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest | grep tag_name | cut -d '"' -f 4 | sed 's/v//')

# Check if version was retrieved
if [ -z "$LATEST_HUGO_VERSION" ]; then
    echo "Error: Could not fetch latest Hugo version"
    exit 1
fi

echo "Installing Hugo version: $LATEST_HUGO_VERSION"

# Determine architecture (M1/MacOS ARM64 vs Intel x86_64)
if [[ "$(uname -m)" == "arm64" ]]; then
    ARCH="arm64"
    EXTENDED="extended"
else
    ARCH="amd64"
    EXTENDED=""
fi

# Set the download URL for macOS
HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${LATEST_HUGO_VERSION}/hugo_${LATEST_HUGO_VERSION}_macOS-${ARCH}.tar.gz"

# Download the tar.gz package
echo "Downloading Hugo..."
curl -L -o /tmp/hugo.tar.gz "$HUGO_URL"

# Check if download was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to download Hugo"
    exit 1
fi

# Extract the tar.gz package
echo "Extracting Hugo..."
mkdir -p /tmp/hugo
tar -xzf /tmp/hugo.tar.gz -C /tmp/hugo

# Move to /usr/local/bin (create directory if needed)
sudo mkdir -p /usr/local/bin

# Move the Hugo binary to /usr/local/bin
sudo mv /tmp/hugo/hugo /usr/local/bin/hugo

# Clean up
rm -rf /tmp/hugo.tar.gz /tmp/hugo

echo "Hugo ${LATEST_HUGO_VERSION} installed successfully!"

# Verify installation
hugo version
