 
# 1. Python Program to Find the Largest Number in a List 
def large_num_list(list_input):
    return sorted(list_input)[-1]

# 2. Python Program to Find the Second Largest Number in a List 
def large_2_num_list(list_input):
    return sorted(list_input)[-2]

# 3. Python Program to Put Even and Odd elements in a List into Two Different Lists. 
def even_odd_list(list_input):
    odd_list=[]
    even_list=[]
    for i in list_input:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return odd_list,even_list
# 4. Python Program to check whether two lists are same. 
def list_is_same(list_input_1,list_input_2):
    if list_input_1==list_input_2:
        return True
    return False
# 5. Python Program to Find the Union of Lists. 
def list_union__(list_input_1,list_input_2):
    for i in list_input_2:
        list_input_1.append(i)
    return list_input_1
# 6. Python Program to Find the Intersection of Lists. 
def list_intersection(list_input1,list_input2):
    a=[]
    for i in list_input1:
        if i in list_input2 and i not in a:
            a.append(i)
    return a


# 7. Python Program to find union and intersection of
#  lists without repetition. 
def list_union_intersection(list_input1,list_input2,option):
    if option==1:
        for i in list_input1:
            if i in list_input2:
                continue
            else:
                list_input2.append(i)
        return list_input2
    if option==2:
        a=[]
        for i in list_input1:
            if i in list_input2 and i not in a:
                a.append(i)
        return a 
    return None
# 8. Python Program to Create a List of Tuples with the First Element as the Number and Second 
# Element as the Square of the Number. 
def list_tuple_square(stop_number):
    a=[]
    for i in range(1,stop_number+1):
        a.append((i,i**2))
    return a

# 9. Python Program to Remove the Duplicate Items from a List. 
def rmv_Duplicate_list(list_input):
    for i in list_input:
        while(list_input.count(i)!=1):
            list_input.remove(i)
    return list_input

# 10.  Python Program to Read a List of Words and Return the Length of the Longest One. 
def list_long_word(word_list_input):
    max_length_string=0
    for i in word_list_input:
        if len(i)>max_length_string:
            max_length_string=len(i)
    return max_length_string


# 1. Python Program to Add a Key-Value Pair to the Dictionary 
def insert_key_val(dictionary_given,input_key,input_val):
    dictionary_given[input_key]=input_val
    return dictionary_given

# 2. Python Program to Concatenate Two Dictionaries Into One 
def update_dict(input_dictionary1,input_dictionary2):
    input_dictionary1.update(input_dictionary2)
    return input_dictionary1

# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not 
def give_key_exist(input_dict,key_entered):
    if key_entered in input_dict.keys():
        return True
    return False

# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form 
# (x,x*x). 
def Gen_dict_num(n):
    genrator={}
    for i in range(n):
        genrator[i]=i*i
    return genrator

# 5. Python Program to Sum All the Items in a Dictionary 
def dict_sum(dict_input):
    if dict_input=={}:
        return None
    sum_num=0
    for i in dict_input.values():
        sum_num=sum_num+i
    return sum_num

# 6. Python Program to Multiply All the Items in a Dictionary
def dict_mul(dict_input):
    if dict_input=={}:
        return None
    sum_mul=1
    for i in dict_input.values():
        sum_mul=sum_mul*i
    return sum_mul
 
# 7. Python Program to Remove the Given Key from a Dictionary 
def dict_remv(dict_input={}):
    if dict_input=={}:
        return None
    sum_num=0
    for i in dict_input.values():
        sum_num=sum_num*i
    return sum_num

# 8. Write a function is_empty(my_dict) that takes a dictionary my_dict and returns True if my_dict 
# is empty and False otherwise. 
def is_empty(my_dict={}):
    if my_dict=={}:
        return True
    return False

# 9.  Write a function make_dict(key_value_list) that takes a list of tuples key_value_list where each 
# tuple is of the form (key, value) and returns a dictionary with these keys and corresponding 
# values.
def make_dict(key_value_list):
    dict_created={}
    # print(key_value_list[0][0])
    for i in range(len(key_value_list[0])):
        dict_created[key_value_list[0][i]]=key_value_list[1][i]
    return dict_created
# 10.  A  simple  substitution  cipher  is  an  encryption  scheme  where  each  letter  in  an  alphabet  to 
# replaced  by  a  different  letter  in  the  same  alphabet  with  the  restriction  that  each  letter's 
# replacement  is  unique.  The  template  for  this  question  contains  an  example  of  a  substitution 
# cipher represented a dictionary CIPHER_DICTIONARY. Your task is to write a function 
# encrypt(phrase,cipher_dict)  that  takes  a  string  phrase  and  a  dictionary  cipher_dict  and  returns 
# the results of replacing each character in phrase by its corresponding value in cipher_dict. 
 
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 
'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 
'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 
'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': 
' ', 'w': 't'}  
#  encrypt("cat", CIPHER_DICT) should return ”km “ 
def enecrypt(string_input,CIPHER_DICT=CIPHER_DICT):
    a=''
    for i in string_input:
        if i in CIPHER_DICT.keys():
            a=a+CIPHER_DICT[i]
    return a
    # for i in range(len(list_str)):
    #     if False==CIPHER_DICT[list_str[i]]:
    #         continue
    #     list_str[i]=CIPHER_DICT[list_str[i]]
    # return ''.join(list_str)

# 11.  Write a function make_cipher_dict(alphabet) that takes a string of unique characters and 
# returns a randomly-generated cipher dictionary for the characters in alphabet . You should use 
# the shuffle() method in the random module to ensure that your returned cipher dictionary is 
# random. 
def make_cipher_dict(alphabet):
    old_alplha=alphabet
    import random
    alph_list=list(alphabet)
    # print(old_alplha)
    print(random.shuffle(alph_list))
    # print(alph_list)

    return(dict(zip(old_alplha,alph_list)))
# 12.  Write a python code to generate grade using dictionary. Dictionary should have student names 
# as keys (assuming names are unique) and subject_name and mark as value. There are 5 subjects 
# for each student. Marks should be converted to grades (90 – 100 A+, 80-89 A etc). 

def Grading_dict(student={}):
    for i in student.values():
        # print(i)
        for j in i.keys():
            # print(j)
            if i[j]>=90:
                i[j]="A+"
                continue
            if i[j]>=80 and i[j]<90:
                i[j]="A"
                continue
            if i[j]>=70 and i[j]<80:
                i[j]="B"
                continue
            if i[j]>=60 and i[j]<70:
                i[j]="c"
                continue
            if i[j]>=50 and i[j]<60:
                i[j]="D"
                continue
            if i[j]>=40 and i[j]<50:
                i[j]="E"
                continue
            if i[j]<40:
                i[j]="F"
                continue

        # print(i)
    return student
 