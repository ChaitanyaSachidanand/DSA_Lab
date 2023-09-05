#Write  a  program  most-recent-file.py  to  find  the  most  recently  modified  file  in  the 
# given  directory.  The  program  should  accept  the  directory  name  as  command-line 
# argument  and  print  path  to  the  file  (not  just  filename)  that  is  most  recently  modified 
# file.
import os
import sys

try:
    Path=sys.argv[1]
except:
    Path = os.getcwd()
os.chdir(Path)
# print(os.listdir(Path))


entries = os.listdir(Path)
# print(entries)
all_file = []
# most_recent_time = 0
for entry in entries:
    if "." in entry:
        all_file.append(entry)
        
        
if all_file:
    print("all file in Direactory:",all_file)
else:
    print("No files found in the directory.")