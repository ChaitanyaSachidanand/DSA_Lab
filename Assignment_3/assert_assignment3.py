from Assignment_3 import *
# 13. Write a function unique to find all the unique elements of a list. 
assert(uniq_element([1,5,5,5,6,7,8,4,5,6,7,8,2,2,2,3,4])==[1, 2, 3, 4, 5, 6, 7, 8])

# 14. Write a function dups to find all duplicates in the list. 
assert(dups([1, 2, 2, 3, 4, 4, 5])==[2, 4])

# 15.  Write  a  function group(list,  size)  that  take  a  list  and  splits  into  smaller  lists  of 
# given size. 
assert(group([1,2,3,4,5,6,7,8,9,0,15,6,89],3)==[[1, 2, 3], [4, 5, 6], [7, 8, 9], [0,15,6],[89]])