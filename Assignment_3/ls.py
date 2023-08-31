# 7. Write a program ls.py that takes path to a directory as command-line argument and 
# prints  all  the  files  in  that  directory. When no  argument  is  specified, it  should  list  the 
# files in the current directory. 

import os
import sys

try:
    Path=sys.argv[1]
except:
    Path = os.getcwd()

print(os.listdir(Path))
# print(Path)