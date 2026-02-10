import sys
import os

def remove_duplicate_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return

    new_lines = []
    found_disable_hljs = False
    for line in lines:
        if "disableHLJS: false" in line:
            if not found_disable_hljs:
                new_lines.append(line)
                found_disable_hljs = True
        else:
            new_lines.append(line)

    if len(lines) != len(new_lines):
        try:
            with open(file_path, 'w') as f:
                f.writelines(new_lines)
            print(f"Removed duplicates from {file_path}")
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")

def is_empty_post(filepath):
    """Check if a post is empty (no meaningful content)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract content after frontmatter
        if content.startswith('---'):
            # Find the closing --- of frontmatter
            match = content.find('---\n', 3)
            if match != -1:
                # Get content after frontmatter
                content_after_fm = content[match+4:]
                # Remove frontmatter and check if content is empty
                content_after_fm = content_after_fm.strip()
                return len(content_after_fm) == 0
        
        # If no frontmatter or other issues, check entire content
        content = content.strip()
        return len(content) == 0
        
    except Exception as e:
        print(f"Error checking if post is empty: {e}")
        return False

def process_file_with_empty_check(filepath):
    """Process file and remove if empty."""
    if is_empty_post(filepath):
        try:
            os.remove(filepath)
            print(f"Removed empty post: {filepath}")
            return True
        except Exception as e:
            print(f"Error removing empty post {filepath}: {e}")
            return False
    else:
        # Process as normal
        remove_duplicate_lines(filepath)
        return True

if __name__ == "__main__":
    for line in sys.stdin:
        filepath = line.strip()
        if os.path.exists(filepath):
            process_file_with_empty_check(filepath)
