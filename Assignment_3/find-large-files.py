# 12. Write a program find-large-files.py to find files recursively in a directory tree that 
# are  larger  than  given  size.  The  program  should  accept  the  directory  and  the  size  as 
# command-line argument. The size can be also be specified with K, M and G suffix for 
# KB, MB and GB respectively. 
import os
import sys

if len(sys.argv) != 3:
    print("Usage: python find-large-files.py <directory_path> <size_in_bytes>")
    sys.exit(1)

def convert_size_to_bytes(size):
    size = size.upper()
    if size.endswith("K"):
        return int(size[:-1]) * 1024
    elif size.endswith("M"):
        return int(size[:-1]) * 1024 * 1024
    elif size.endswith("G"):
        return int(size[:-1]) * 1024 * 1024 * 1024
    else:
        return int(size)
    
directory_path = sys.argv[1]
min_size_bytes = convert_size_to_bytes(sys.argv[2])

large_files = []

for root, _, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            file_size = os.path.getsize(file_path)
            if file_size > min_size_bytes:
                large_files.append(file_path)
        except Exception as e:
            continue  # Skip files with errors

if large_files:
    print("Large files in the specified directory:")
    for file in large_files:
        print(file)
else:
    print("No large files found in the specified directory.")
