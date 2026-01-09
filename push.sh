#!/bin/bash

# Check if there are any uncommitted changes
#if ! git diff-index --quiet HEAD --; then
#    echo "You have uncommitted changes. Please commit them or use 'git stash' before running this script."
#    exit 1
#fi

# Get the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Git pull
#git pull --ff || { echo "Git pull failed. Aborting."; exit 1; }

# Check for uncommitted changes after pull
#if ! git diff-index --quiet HEAD --; then
#    echo "There are uncommitted changes after the pull. Please handle them before proceeding."
#    exit 1
#fi

# Prompt the user for a commit message
#read -p "Enter commit message: " commit_message
if [ -z "$commit_message" ]; then
    commit_message="."
fi

# Git add, commit, and push
git add .
git commit -m "$commit_message" || { echo "Git commit failed. Aborting."; exit 1; }
git push -u origin "$current_branch" || { echo "Git push failed. Aborting."; exit 1; }
echo "Changes pushed successfully to $current_branch."

