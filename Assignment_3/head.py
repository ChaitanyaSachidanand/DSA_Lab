import sys

if len(sys.argv) != 2:
    print("Usage: python wc.py <filename>")
    
filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        # print(file)
        lines = 0
        
        for line in file:
            # print(type(line))
            lines += 1
            
            if lines>5: 
                print("the file has more that 5 lines so its exiting")
                exit(0)
            print(f"line No.{lines}: ",line)
        
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

