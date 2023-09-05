# 10.  Write  a  program  files-only.py  to  find  only  file  and  not  sub  directories.  Pass 
# directory name as command line argument. 


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