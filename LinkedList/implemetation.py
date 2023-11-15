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
def remove_duplicates(linked_list):
    # Check if the linked list is empty or has only one node
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list

    # Create a set to store unique elements
    unique_elements = set()

    # Traverse the linked list
    current = linked_list.head
    previous = None
    while current is not None:
        # Check if the current element is a duplicate
        if current.data in unique_elements:
            # Remove the duplicate element by updating the next pointer of the previous node
            previous.next = current.next
        else:
            # Add the current element to the set of unique elements
            unique_elements.add(current.data)
            previous = current

        current = current.next

    return linked_list
a = LinkedList_()
for i in range(10):
    a.insert_head(i)
    a.insert_head(i)
a.print_listH()
x=remove_duplicates(a)
x.print_listH()
'''
8. Find middle element of linked list without iterating all elements. 
'''
def find_middle_element(linked_list):
    temp=linked_list.head
    count=(lambda x: x//2 - 1 if x % 2 == 0 else x//2)(linked_list.count)
    mid_element=0

    while count//2!=mid_element:
        temp=temp.next
        mid_element+=1
    
    return temp.data,mid_element
mid,index__=find_middle_element(x)
x.print_listH()
print("Middle most element in linked list is:",mid,"at index:",index__)
'''
9. Find whether linked list contains cycle. 
'''
def has_cycle(linked_list):
    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False

temp = LinkedList_()
temp.insert_head(1)
node2 = LinkedList_()
node2.insert_head(2)
node3 = LinkedList_()
node3.insert_head(3)
node4 = LinkedList_()
node4.insert_head(4)
node5 = LinkedList_()
node5.insert_head(5)

temp.head.next = node2
node2.head.next = node3
node3.head.next = node4
node4.head.next = node5
node5.head.next = node2  # Creating a cycle by pointing the last node to node2

# Test the has_cycle function
if has_cycle(temp):
    print("The linked list contains a cycle")
else:
    print("The linked list does not contain a cycle") #testing yet to be done