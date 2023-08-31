
# 8.  Write  a  program  largest-file.py  to  find  the  largest  file  in  the  given  directory.  The 
# program  should  accept  the  directory name  as  command-line  argument  and  print path 
# to the file (not just filename). 

import os
import sys

try:
    Path=sys.argv[1]
except:
    Path = os.getcwd()
os.chdir(Path)
# print(os.listdir(Path))
size_file_dict={}
for i in os.listdir(Path):
    size_file_dict[os.path.getsize(i)]=i
print("The file with max size is:",max(size_file_dict.keys()))
print("The file path is : ",Path," file name is : ", size_file_dict[max(size_file_dict.keys())])