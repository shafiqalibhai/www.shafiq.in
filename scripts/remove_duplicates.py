import sys

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

if __name__ == "__main__":
    for line in sys.stdin:
        remove_duplicate_lines(line.strip())