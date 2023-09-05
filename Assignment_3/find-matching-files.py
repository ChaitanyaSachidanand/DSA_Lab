# 11. Write a program find-matching-files.py to find files recursively in a directory tree 
# matching  given  wildcard  pattern.  The  program  should  accept  the  directory  and  the 
# pattern as command-line argument. 


# import os
# import sys

# try:
#     Path=sys.argv[1]
# except:
#     Path = os.getcwd()
# # print(os.walk(Path))
# # print(os.listdir(Path))


# entries = os.listdir(Path)
# directoryAndSub=[]
# for x in entries:
#     if '.' not in x:
#         directoryAndSub.append(x)
# print(directoryAndSub)
# # print(entries)
# all_file = []
# dir_present = []
# # most_recent_time = 0
# for entry in entries:
#     if "." in entry:
#         all_file.append(entry)
        
        
# if all_file:
#     print("all file in Direactory:",all_file)
# else:
#     print("No files found in the directory.")

import os
import sys

if len(sys.argv) != 3:
    print("Usage: python find-matching-files.py <directory_path> <file_pattern>")
    sys.exit(1)

# re.findall()
directory_path = sys.argv[1]
file_pattern = sys.argv[2]


def find_patteren_func(directory_path,file_pattern):
    for i in os.listdir(directory_path):
        if "." in i:
            if file_pattern in i:
                print("In directory: '", directory_path,"' the pattern '",file_pattern,"'with file name: '",i,"'")
        else:
            find_patteren_func(directory_path+'\\'+i,file_pattern)

find_patteren_func(directory_path,file_pattern)
