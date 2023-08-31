from functions_2 import *
# 1. Python Program to Find the Largest Number in a List
assert(large_num_list([1,4,7,2,5,8,9,6,3])==9)

# 2. Python Program to Find the Second Largest Number in a List 
assert(large_2_num_list([1,4,7,2,5,8,9,6,3])==8)

# 3. Python Program to Put Even and Odd elements in a List into Two Different Lists. 
assert(even_odd_list([1,4,7,2,5,8,9,6,3])==([1,7,5,9,3],[4,2,8,6]))
# 4. Python Program to check whether two lists are same. 
assert(list_is_same([1,4,7,2,5,8,9,6,3],[1,4,7,2,5,8,9,6,3])==True)
assert(list_is_same([1,4,7,2,5,8,9,6,3],[3,1,7,2,8,8,9,6,3])==False)

# 5. Python Program to Find the Union of Lists. 

# print(list_union__([1,2,3,4,5,6,7],[8,9,0]))
assert(list_union__([1,2,3,4,5,6,7],[8,9,0])==[1,2,3,4,5,6,7,8,9,0])

# 6. Python Program to Find the Intersection of Lists. 
assert(list_intersection([1,4,7,2,5,8,9,6,3],[8,9,0])==[8,9])
# 7. Python Program to find union and intersection of lists without repetition. 

assert(list_union_intersection([1,4,7,2,5,8,9,6,3],[8,9,0],2)==[8,9])
assert(list_union_intersection([1,4,7,2,5,8,9,6,3],[8,9,0],1)==[8, 9, 0, 1, 4, 7, 2, 5, 6, 3])
# 8. Python Program to Create a List of Tuples with the First Element as the Number and Second 
# Element as the Square of the Number. 
assert(list_tuple_square(10)==[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)])
# 9. Python Program to Remove the Duplicate Items from a List. 
assert(rmv_Duplicate_list([1,4,1,7,2,3,5,8,9,9,6,3])==[4, 1, 7, 2, 5, 8, 9, 6, 3])
assert(rmv_Duplicate_list([1,1,4,1,7,2,3,5,8,8,8,9,9,9,6,3,1,1])==[4, 7, 2, 5, 8, 9, 6, 3, 1])
# 10.  Python Program to Read a List of Words and Return the Length of the Longest One. 
assert(list_long_word(['zabcdefghij','abc','hijkl','ooqwe'])==11)
 
# 1. Python Program to Add a Key-Value Pair to the Dictionary 
assert(insert_key_val({1:'apple',2:'banana'},10,'dragon fruit')=={1:'apple',2:'banana',10:'dragon fruit'})

# 2. Python Program to Concatenate Two Dictionaries Into One 
assert(update_dict({1:'apple',2:'banana'},{10:'dragon fruit'})=={1:'apple',2:'banana',10:'dragon fruit'})

# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not 
assert(give_key_exist({1:'apple',2:'banana',10:'dragon fruit'},10)==True)
 
assert(give_key_exist({1:'apple',2:'banana',10:'dragon fruit'},90)==False)
# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form 
# (x,x*x). 
assert(Gen_dict_num(10)=={0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81})

# 5. Python Program to Sum All the Items in a Dictionary
assert(55==dict_sum({0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}))
# 6. Python Program to Multiply All the Items in a Dictionary 
assert(14400==dict_mul({1: 1, 2: 4, 3: 9, 4: 16, 5: 25}))

# 7. Python Program to Remove the Given Key from a Dictionary 
# 8. Write a function is_empty(my_dict) that takes a dictionary my_dict and returns True if my_dict 
# is empty and False otherwise. 
# 9.  Write a function make_dict(key_value_list) that takes a list of tuples key_value_list where each 
# tuple is of the form (key, value) and returns a dictionary with these keys and corresponding 
# values.  
assert(make_dict((('Ravi','sam','bon','zoro','luffy'),('normal guy','A father','copy devil fruit','World gratest swords man','king of Pirates')))=={'Ravi': 'normal guy', 'sam': 'A father', 'bon': 'copy devil fruit', 'zoro': 'World gratest swords man', 'luffy': 'king of Pirates'})

# 10.  A  simple  substitution  cipher  is  an  encryption  scheme  where  each  letter  in  an  alphabet  to 
# replaced  by  a  different  letter  in  the  same  alphabet  with  the  restriction  that  each  letter's 
# replacement  is  unique.  The  template  for  this  question  contains  an  example  of  a  substitution 
# cipher represented a dictionary CIPHER_DICTIONARY. Your task is to write a function 
# encrypt(phrase,cipher_dict)  that  takes  a  string  phrase  and  a  dictionary  cipher_dict  and  returns 
# the results of replacing each character in phrase by its corresponding value in cipher_dict. 
 
#   CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 
# 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 
# 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 
# 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': 
# ' ', 'w': 't'} 
#  encrypt("cat", CIPHER_DICT) should return ”km “ 
assert(enecrypt('king of pirates, worlds gratest swordsman')=='xiafbypbvigm uobtygndobfgm uo botygdowma')
 
# 11.  Write a function make_cipher_dict(alphabet) that takes a string of unique characters and 
# returns a randomly-generated cipher dictionary for the characters in alphabet . You should use 
# the shuffle() method in the random module to ensure that your returned cipher dictionary is  random. 
print(make_cipher_dict("hello world"))

# 12.  Write a python code to generate grade using dictionary. Dictionary should have student names 
# as keys (assuming names are unique) and subject_name and mark as value. There are 5 subjects 
# for each student. Marks should be converted to grades (90 – 100 A+, 80-89 A etc). 
assert(Grading_dict({"Chaitanya":{"Math":81,"English":85,"BDA":92,"APS":100},
                    "Luffy":{"Math":20,"English":60,"BDA":81,"APS":59},
                     "Zoro":{"Math":77,"English":81,"BDA":31,"APS":82},})==
                     {'Chaitanya': {'Math': 'A', 'English': 'A', 'BDA': 'A+', 'APS': 'A+'}, 
                      'Luffy': {'Math': 'F', 'English': 'c', 'BDA': 'A', 'APS': 'D'}, 
                      'Zoro': {'Math': 'B', 'English': 'A', 'BDA': 'F', 'APS': 'A'}}) 
 