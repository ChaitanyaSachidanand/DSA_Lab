 
# 1. Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable. 
def swap_num(num1,num2):
    return num2,num1

# 2. Python Program to Check Whether a Number is Positive or Negative. 
def If_positve(num1):
    return num1>-1
# 3. Python Program to Print all Numbers in a Range Divisible by a Given Number. [ if range is from 1 
# to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ] 
def print_num_in_range(range_num,div_num):
    a=[]
    for i in range(0,range_num+1,div_num):
        a.append(i)
    return a
# 4. Python Program to Read Two Numbers and Print Their Quotient and Remainder.
def quotient_reminder(divident, divisor):
    quotient=divident//divisor
    reminder=divident%divisor
    return quotient,reminder 
# 5. Python Program to Print Odd Numbers Within a Given Range.
def Odd_num(range_num):
    a=[]
    for i in range(1,range_num,2):
        a.append(i)
    return a 
# 6. Python Program to Find the Sum of Digits in a Number. 
def sum_digits(Number):
    sum=0
    while(Number!=0):
        n=Number%10
        sum=sum+n
        Number=Number//10
    return sum
# 7. Python Program to Find the Smallest Divisor of an Integer.
def smalls_divisor(number):
    for i in range(2,10):
        if number%i==0: return i 
# 8. Python Program to Read a number n and Compute n+nn+nnn. 
def n_compute_sum(n,count):
    if count==0: return  0
    return n**count + n_compute_sum(n,count-1)
    
# 9. Python Program to Reverse a Given Number. 
def reverse_num(Number):
    sum=0
    while(Number!=0):
        sum=sum*10
        n=Number%10
        sum=sum+n
        Number=Number//10    
    return sum
# 10.  Python Program to Calculate the Average of Numbers in a Given List. \
def avg_of_list(list_num):
    return sum(list_num)/len(list_num)

# 11.  Python Program to Count the Number of Digits in a Number.
def count_digits(Number):
    return len(str(Number))
# 12.  Python Program to Check if a Number is a Palindrome.
def check_num_Palindrome(Number):
    if reverse_num(Number)==Number: return 1
    return 0 
# 13.  Python Program to print the number of occurrence of a sub string in a given string. 
def sub_string_find(sub_str,main_str):
    if sub_str in main_str: return 1
    return 0
# 14.  Python program to print the lowest index in the string where substring sub is found within the 
# string. 
def sub_string_index(sub_str,main_str):
    if sub_str in main_str: return main_str.index(sub_str)
    return 0
# 15.  Python Program to return true if all characters in the string are alphabetic and there is at least 
# one other character, False. 
def check_if_string(string_content):
    for i in string_content:
        if ord(i)<65 or ord(i)>90 and ord(i)<97 or ord(i)>172: return False
    return True 
# 16.  Python Program to Replace all Occurrences of ‘a’ with $ in a String.
def String_replace(main_string,replacemt):
    return main_string.replace('a',replacemt) 
# 17.  Python Program to Count the Number of Vowels in a String.
def vowel_count(string_inputed):
    return string_inputed.count('a')+string_inputed.count('e')+string_inputed.count('i')+string_inputed.count('o')+string_inputed.count('u') 
# 18.  Python Program to Take in a String and Replace Every Blank Space with Hyphen. 
def String_replace_hyphen(main_string):
    return main_string.replace(' ','-')
# 19.  Python Program to find the length of string without using any built-in functions. 
def length_string(string_input):
    cout=0
    for i in string_input:
        cout=cout+1
    return cout

# 20.  Python Program to Take in Two Strings and Display the Larger String without Using Built-in 
# Functions. 
def greater_dtring(sample_string1,sample_string2):
    if length_string(sample_string1)>length_string(sample_string2): return sample_string1
    else: return sample_string2

# 21.  Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a 
# String. 
def count_up_low_string(sample_string):
    count_up=0
    count_low=0
    for i in sample_string:
        if i.isupper(): count_up=count_up+1
        if i.islower(): count_low=count_low+1
    return count_low,count_up
# 22.  Python Program to Calculate the Number of Digits and Letters in a String. 
def calculate_digit_letter(sample_string):
    count_alp=0
    count_dig=0
    for i in sample_string:
        if i.isalpha(): count_dig=count_dig+1 
        if i.isdigit(): count_alp=count_alp+1
    return count_alp,count_dig
# 23.  Python Program to check whether a full pattern (not sub string) is present in the given sentence.
def full_pattern_sentance(sentance_,word_):
    if (" "+word_ or word_+" " ) in sentance_:
        return True
    else:
        return False

# 24.  Cumulative sum of a list [1, 2, 4, ...] is defined as  [1, 3, 7, . . .] Write a function 
# cumulative_sum() to compute cumulative sum of a list 
def cumulative_sum(list_num):
    sum_list=[]
    for i in range(len(list_num)):
        if list_num[i]==list_num[-1]: break
        if i==0: 
            sum_list.append(list_num[i])
            continue
        sum_list.append(list_num[i]+sum(sum_list))
    return sum_list

# 25.  Write a program to generate 10 random integers. 
import random
def get_random_num(num):
    for i in range(num):
        print(random.randint(1,100),end=' ')


# 26.  Write a program to generate 10 random integers between 1 to 20 (both inclusive). 
def get_random_range(start,stop,total_num):
    for i in range(total_num):
        print(random.randint(start, stop), end=" ")

# 27.  Write a program to generate 5 random integers between 1 to 20 such that numbers should be 
# unique.
def get_random_range_uniq(start,stop,total_num):
    for i in range(total_num):
        print(random.randrange(start, stop,1), end=" ")
 
# 28.  Write a program to generate 10 random numbers between 1 to 100 such that there should one 
# number between 1 to 10 one number between 11 to 20 etc. 
def get_random_range_seial(start,stop,total_num):
    for i in range(total_num):
        print(random.randrange(start+i*10, (i+1)*10), end=" ")