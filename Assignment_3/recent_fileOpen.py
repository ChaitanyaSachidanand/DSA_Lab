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


entries = os.scandir(Path)
most_recent_file = None
most_recent_time = 0
for entry in entries:
    if entry.is_file():
        modification_time = entry.stat().st_mtime
        if modification_time > most_recent_time:
            most_recent_time = modification_time
            most_recent_file = entry.path
        
if most_recent_file:
    print("Most recently modified file:",most_recent_file)
else:
    print("No files found in the directory.")