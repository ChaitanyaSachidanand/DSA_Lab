class LinkedList_():
    '''
    Linked List assignments 
    1. Create Doubly Linked List class with following functionalities: 
    a. Add at head 
    b. Add at tail 
    c. Delete at head 
    d. Delete at tail 
    e. Add after given data 
    f. Delete after given data 
    g. Search an element
    '''
    class Node:
        def __init__(self,ele):
            self.data=ele
            self.prev=None
            self.next=None


    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def is_Empty(self):
        if self.count == 0:
            return True
        else:
            return self.count

    def inset_head(self,element):

        new_node = self.Node(element)
        if self.count==0:
            self.head=new_node
            self.tail=self.head
            self.count+=1
            return
        link = self.head
        self.head=new_node
        link.prev=self.head
        self.head.next=link
        # 
        self.count+=1



    def insert_tail(self,element):
        new_node = self.Node(element)
        if self.count==0:
            self.head=new_node
            self.tail=self.head
            self.count+=1
            return
        link = self.tail
        self.tail=new_node
        self.tail.prev=link
        link.next=self.tail

        self.count+=1

    def del_head(self):
        if self.count==0:
            print("No element present")
            return
        elif self.count==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None

        self.count-=1
        


    def del_tail(self):
        if self.count==0:
            print("No element present")
            return
        elif self.count==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None

        self.count-=1

    def print_listF(self):
        # return
        temp = self.head
        if self.count==0:
            print("No elements present")
        while temp!=None:
            print(temp.data," | ",end="   ")
            temp = temp.next
        print()
    def print_listL(self):
        # return
        temp = self.tail
        if self.count==0:
            print("No elements present")
        while temp!=None:
            print(temp.data," | ",end="   ")
            temp = temp.prev
        print()
    
    def add_after_givenData(self,elemet,addelement):
        new_node=self.Node(addelement)
        if self.count==0:
            print("No elements present")
        temp=self.head
        # local_count=0
        while temp.next!=None and temp.data==elemet:

            temp=temp.next
            # local_count+=1
        next=temp.next


        pass

abc = LinkedList_()
abc.print_listL()
abc.insert_tail(44)
abc.inset_head(10)
abc.print_listL()
abc.insert_tail(5)
abc.print_listF()
abc.insert_tail(21)
abc.inset_head(47)
abc.inset_head(78)
abc.insert_tail(8)
abc.print_listF()
abc.del_head()
abc.del_head()
abc.del_head()
abc.print_listL()
abc.del_tail()
abc.del_tail()
abc.del_tail()
abc.print_listL()
abc.inset_head(358)
abc.insert_tail(8243)
abc.print_listF()







    