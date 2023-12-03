import os
import sys

EXCLUDE_DOTS = True
EXCLUDE_UNDERSCORES = True
TELL_ALWAYS = False
SORTED = False

excludes = []

if len(sys.argv) > 1:
    excludes.extend(sys.argv[1:])

if excludes:
    print("Excluding anything that matches: " + " ".join(['"'+exclude+'"' for exclude in excludes]))

total_size = 0
total_lines = 0
total_code_size = 0
total_code_lines = 0
scanned_files = 0
excluded_files = 0

size_index = {}

for root, dirs, files in os.walk("."):
    for name in files:
        bad = False

        for exclude in excludes:
            if exclude in name:
                excluded_files += 1
                bad = True

        path = os.path.join(root, name)
        
        if EXCLUDE_DOTS or EXCLUDE_UNDERSCORES:
            split_path = path.split("/")
            for item in split_path:
                if item[0] == "." and EXCLUDE_DOTS and item != ".":
                    bad = True
                if item[0] == "_" and EXCLUDE_UNDERSCORES:
                    bad = True

        if bad:
            continue

        try:
            with open(path, "r") as f:
                content = f.read()

        except UnicodeDecodeError:
            if TELL_ALWAYS:
                print(f"{name} is not text!")

        else:
            size = 0
            lines = 0
            code_size = 0
            code_lines = 0

            for line in content.splitlines():
                size += len(line)
                lines += 1
                line_stripped = line.strip()
                if line_stripped and len(line_stripped) > 1 and line_stripped[0] != "#":
                    code_size += len(line_stripped)
                    code_lines += 1

            total_size += size
            total_lines += lines
            total_code_size += code_size
            total_code_lines += code_lines

            scanned_files += 1

            size_index[name] = code_lines

            print(f"{name}: {size}B {lines}l, {code_size}Bc {code_lines}lc")

if SORTED:
    print("\nSORTED TIME!")
    # not mine lol
    sorted_dict = {k: v for k, v in sorted(size_index.items(), key=lambda item: item[1], reverse=True)}
    for key in sorted_dict:
        print(f"{key} has {sorted_dict[key]} lines")

print(f"\nScanned {scanned_files} text files\nExcluded {excluded_files} based on filter")
print(f"\nTotal size: {total_size}\nTotal lines: {total_lines}\nTotal size (code only): {total_code_size}\nTotal lines (code only): {total_code_lines}")
                
