from Linkedlist import LinkedList_
'''_
2. Assume that we have two linked lists. Elements in individual list are unique. There may 
be identical elements across linked lists. Create a third list which contains only common 
elements across first two lists. '''

a = LinkedList_()
b=LinkedList_()
for i in range(10):
    a.insert_head(i)
for j in range(6,15):
    b.insert_tail(j)
# a.print_listH()
a.print_listH()
b.print_listH()

def two_linklist_common(a1, b2):
    c = LinkedList_()
    current = a1.head
    
    while current.next != None:
        if b2.search_element(current.data)==current.data:
            c.insert_tail(current.data)
        current=current.next
    return c

c = two_linklist_common(a, b)
c.print_listH()

'''
3. Find the sum of last ‘n’ nodes in single linked list. Where ‘n’ will be given. Sum should be 
calculated with one iteration. 
'''

def sum_last_n_nodes(n):
    a.print_listH()
    print(a.count)
    count=a.count-n
    sum=0
    temp_count=0
    temp=a.head
    
    while temp.next!=None:
        if temp_count>=count:
            sum=sum+temp.data
        temp=temp.next
        temp_count+=1
    return sum

print("Sum of last n nodes",sum_last_n_nodes(3))
'''
4. Reverse the single linked list. 
'''
def reverse_linked_list(a):
    rev_list=LinkedList_()
    print(a.print_listH())
    temp=a.head
    while temp.next is not None:
        rev_list.insert_head(temp.data)
        temp=temp.next
    rev_list.insert_head(temp.data)
    return rev_list
z=LinkedList_()
for _ in range(20):
    z.insert_tail(_)
    z.print_listH()
print(reverse_linked_list(z).print_listH())
'''
5. Implement  split()  function  which  splits  given  linked  list  into  two  separate  linked  lists 
containing alternate elements from original list.'''
def split_linked_list(linked_list):
    # Create two new linked lists to store the alternate elements
    list1 = LinkedList_()
    list2 = LinkedList_()

    current = linked_list.head
    count = 0
    while current is not None:
        if count % 2 == 0:
            list1.insert_tail(current.data)
        else:
            list2.insert_tail(current.data)

        current = current.next
        count += 1

    return list1, list2
print("splitting linked list")
x,y=split_linked_list(a)
print(x.print_listH())
print(y.print_listH())
''' 
6. Check whether given linked list is palindrome or not. 
'''
def is_palindrome(linked_list):
    current1 = linked_list.head
    current2 = reverse_linked_list(linked_list)
    current2=current2.head
    while current2 is not None:
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next
    return True


l_list = LinkedList_()
l_list.insert_tail(1)
l_list.insert_tail(2)
l_list.insert_tail(3)
l_list.insert_tail(2)
l_list.insert_tail(1)

if is_palindrome(l_list):
    print("The linked list is a palindrome")
else:
    print("The linked list is not a palindrome")
'''
7. Write  an  efficient  code  to  remove  duplicate  elements  from  single  linked  list.  (you  can 
make use of built in data structure “set”). '''

'''
8. Find middle element of linked list without iterating all elements. 
'''
'''
9. Find whether linked list contains cycle. 
'''