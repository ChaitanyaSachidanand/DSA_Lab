# 4. Write a program sumfile.py that takes a filename as argument and prints sum of all 
# numbers  in  that  file.  It  is  assumed  that  the  file  will  only  have  one  number  in  every 
# line. 
import sys

filename = sys.argv[1]

try:
    total_sum = sum(float(line.strip()) for line in open(filename))
    print("Sum of numbers:", total_sum)
except Exception as e:
    print("An error occurred:", e)
    