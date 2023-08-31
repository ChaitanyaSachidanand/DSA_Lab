'''
1. Write a program cat.py that takes a filename as command-line argument and prints 
all the contents of that file. 
'''
import sys

if len(sys.argv) != 2:
    print("Usage: python cat.py <filename>")
    

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

