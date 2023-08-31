# 5.  Write  a  program  grep.py  that  takes  a  pattern  and  a  filename  as  command-line 
# argument and prints all the lines in the file that contain given pattern. 
import sys

if len(sys.argv) != 2:
    print("Usage: python wc.py <filename>")
    
filename = sys.argv[1]
pattern = sys.argv[2]

try:
    with open(filename, 'r') as file:
        # print(file)
        lines = 0
        
        for line in file:
            # print(type(line))
            lines += 1
            
            if pattern in line: 
                print(f"line No.{lines}: ",line)
        
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

