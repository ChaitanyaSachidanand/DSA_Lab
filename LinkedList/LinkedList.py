class LinkedList_():
    '''
    Linked List assignments 
    1. Create singly Linked List class with following functionalities: 
    a. Add at head 
    b. Add at tail 
    c. Delete at head
    d. Delete at tail 
    e. Add after given data 
    f. Delete after given data 
    g. Search an element
    '''
    class Node:
        def __init__(self,ele=None):
            self.data=ele
            # self.prev=None
            self.next=None


    def __init__(self):
        self.head = None
        # self.head.Llink =None
        # self.head.Rlink =None
        self.tail = None
        self.count = 0

    def insert_head(self,val):
        ''' a. Add at head '''
        new_node=self.Node(val)
        if self.count==0:
            self.tail=self.head=new_node
            self.count+=1
            return
        new_node.next=self.head
        self.head=new_node
        self.count+=1
    
    def insert_tail(self,val):
        '''b. Add at tail '''
        new_node=self.Node(val)
        if self.count==0:
            self.tail=self.head=new_node
            self.count+=1
            return
        self.tail.next=new_node
        self.tail=new_node
        self.count+=1
    
    def del_head(self):
        if self.count==0:
            print("No element")
        elif self.count==1:
            del_ele=self.head.data
            self.head=self.tail=None
            self.count-=1
        else:
            del_ele=self.head.data
            self.head=self.head.next
            self.count-=1
        return del_ele

    def del_tail(self):
        if self.count==0:
            print("No element")
        elif self.count==1:
            del_ele=self.tail.data
            self.head=self.tail=None
            self.count-=1
        else:
            del_ele=self.tail.data
            temp=self.head
            while temp.next!=self.tail:
                temp=temp.next
            self.tail=temp
            
            self.tail.next = None
            self.count-=1
        return del_ele
        
    def del_after_given(self, value):
        '''
    f. Delete after given data 

    '''
        if self.count == 0:
            print("No element")
        else:
            temp = self.head
            while temp.next is not None:
                if temp.data == value:
                    break
                temp = temp.next
            if temp.next is None:
                print("Given value not found")
            else:
                temp.next = temp.next.next
            self.count -= 1

    def add_after_given(self, val,element):
        '''
    e. Add after given data 
        Add element val: "elemt to add" after the element 
        element:"element from where to add"'''
        new_node = self.Node(val)
        if self.count == 0:
            print("No element")
            self.head=self.tail=new_node

        else:
            temp = self.head
            while temp.next is not None and temp.data != element:
                temp = temp.next
            if temp.next is None:
                temp.next=new_node
                new_node.next=None
                self.tail=new_node
            else:
                ttemp = temp.next
                temp.next =new_node
                new_node.next = ttemp
        self.count += 1
        
    def print_listH(self):
        if self.count==0:
            print("No ele")
        temp=self.head
        while temp.next!=None:
            print(temp.data," | ",end="")
            temp=temp.next
        print(temp.data,"\n")

    def search_element(self,element):
        '''
    g. Search an element'''
        if self.count==0:
            print("No ele")
        temp= self.head
        count=0
        while temp.next!=None and temp.data!=element:
            temp=temp.next
            count+=1
        if temp.data==element:
            print("element:", element,"found in postion: ",count)
            return element
        print("element: ",element," NOT Found")
        return -1



# abc = LinkedList_()
# abc.insert_head(10)
# abc.print_listH()
# abc.insert_head(47)
# abc.insert_head(7)
# abc.insert_tail(0)
# abc.del_head()
# abc.insert_head(120)
# abc.print_listH()
# abc.del_head()
# abc.print_listH()
# abc.insert_head(49)
# abc.insert_head(71)
# abc.print_listH()
# abc.del_tail()
# abc.del_tail()
# abc.print_listH()
# abc.insert_head(29)

# abc.insert_head(77)
# abc.print_listH()
# abc.del_after_given(29)
# abc.insert_tail(1256)
# abc.search_element(49)
# abc.add_after_given(99,49)
# abc.print_listH()
# abc.search_element(77)
# abc.add_after_given(7995,2)
# abc.print_listH()