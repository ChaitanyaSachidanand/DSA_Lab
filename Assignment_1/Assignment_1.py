from Assignment_1.functions_1 import *
# 1. Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable. 
assert(swap_num(15,90)==(90,15))

# 2. Python Program to Check Whether a Number is Positive or Negative. 
assert(If_positve(-58)==False)
assert(If_positve(756)==True)

# 3. Python Program to Print all Numbers in a Range Divisible by a Given Number. [ if range is from 1 
# to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ] 
assert(print_num_in_range(20,4)==[0,4,8,12,16,20])
assert(print_num_in_range(10,3)==[0,3,6,9])

# 4. Python Program to Read Two Numbers and Print Their Quotient and Remainder. 
assert(quotient_reminder(10,2)==(5,0))
assert(quotient_reminder(25,3)==(8,1))

# 5. Python Program to Print Odd Numbers Within a Given Range. 
assert(Odd_num(20)==[1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

# 6. Python Program to Find the Sum of Digits in a Number. 
assert(sum_digits(12345)==15)
assert(sum_digits(123456)==21)
# 7. Python Program to Find the Smallest Divisor of an Integer. 
assert(smalls_divisor(12388645)==5)
assert(smalls_divisor(15166)==2)
# 8. Python Program to Read a number n and Compute n+nn+nnn. 
assert(n_compute_sum(4,4)==340)
assert(n_compute_sum(3,3)==39)
# 9. Python Program to Reverse a Given Number. 
assert(reverse_num(12345)==54321)
assert(reverse_num(147852)==258741)

# 10.  Python Program to Calculate the Average of Numbers in a Given List. 
assert(avg_of_list([1,2,3,4,5])==3)
# 11.  Python Program to Count the Number of Digits in a Number. 
assert(count_digits(12345)==5)
# 12.  Python Program to Check if a Number is a Palindrome. 
assert(check_num_Palindrome(123321)==True)
assert(check_num_Palindrome(123456)==False)
# 13.  Python Program to print the number of occurrence of a sub string in a given string. 
assert(sub_string_find('ab','abdevil')==1)
assert(sub_string_find("aaa",'abcdmanda')==0)
# 14.  Python program to print the lowest index in the string where substring sub is found within the 
# string. 
assert(sub_string_index('all','hai all of u')==4)

# 15.  Python Program to return true if all characters in the string are alphabetic and there is at least 
# one other character, False.
assert(check_if_string('HelloThere')==True)
assert(check_if_string('Hello welcome')==False)
# 16.  Python Program to Replace all Occurrences of ‘a’ with $ in a String. 
assert(String_replace('area of America ',"$")=='$re$ of Americ$ ')
# 17.  Python Program to Count the Number of Vowels in a String. 
assert(vowel_count('apple a day')==4)
# 18.  Python Program to Take in a String and Replace Every Blank Space with Hyphen.
assert(String_replace_hyphen("how is the food")=="how-is-the-food") 
# 19.  Python Program to find the length of string without using any built-in functions. 
assert(length_string('how is it?')==10)
# 20.  Python Program to Take in Two Strings and Display the Larger String without Using Built-in 
# Functions.
assert(greater_dtring('how are you','where are you now')=='where are you now')
# 21.  Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a 
# String. 
assert(count_up_low_string("How is THe weather")==(12,3)) 
# 22.  Python Program to Calculate the Number of Digits and Letters in a String. 
assert(calculate_digit_letter('this1234')==(4,4))
# 23.  Python Program to check whether a full pattern (not sub string) is present in the given sentence. 
assert(full_pattern_sentance("How is the birthdays party","day")==False)
assert(full_pattern_sentance("How is the birthdays party","birthday")==True)
# 24.  Cumulative sum of a list [1, 2, 4, ...] is defined as  [1, 3, 7, . . .] Write a function 
# cumulative_sum() to compute cumulative sum of a list 
assert(cumulative_sum([1,2,3,4,5,6,7,8,9])==[1, 3, 7, 15, 31, 63, 127, 255])

# 25.  Write a program to generate 10 random integers. 
print(get_random_num(10))
# 26.  Write a program to generate 10 random integers between 1 to 20 (both inclusive). 
print(get_random_range(1,20,10))
# 27.  Write a program to generate 5 random integers between 1 to 20 such that numbers should be 
# unique.
print(get_random_range_uniq(1,20,5))
 
# 28.  Write a program to generate 10 random numbers between 1 to 100 such that there should one 
# number between 1 to 10 one number between 11 to 20 etc. 
print(get_random_range_seial(1,100,10))