'''
# 6.  Write  a  program  copyfile.py  to  copy  one  file  to  another.  It  should  accept  two 
# filenames as command-line arguments and copies the first one into the second. 

'''
import sys

# if len(sys.argv) != 2:
    # print("Usage: python cat.py <filename>")
    

source_file = sys.argv[1]
destination_file = sys.argv[2]

try:
    with open(source_file, 'r') as file:
        contents = file.read()
        with open(destination_file,'w') as dest_file:
            dest_file.write(contents)
        # print(contents)
except FileNotFoundError:
    print(f"File '{source_file}' not found.")
    print(f"File '{destination_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

