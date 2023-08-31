import sys

if len(sys.argv) != 2:
    print("Usage: python wc.py <filename>")
    
filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        # print(file)
        lines = 0
        words = 0
        chars = 0
        
        for line in file:
            # print(type(line))
            lines += 1
            words += len(line.split())
            chars += len(line)
        
        print(f"Lines: {lines}")
        print(f"Words: {words}")
        print(f"Characters: {chars}")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

