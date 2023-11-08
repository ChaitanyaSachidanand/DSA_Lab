class LinkedList_():
    '''
    Linked List assignments 
    1. Create singly Linked List class with following functionalities: 


    d. Delete at tail 
    e. Add after given data 
    f. Delete after given data 
    g. Search an element
    '''
    class Node:
        def __init__(self,ele):
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
            return
        self.tail.next=new_node
        self.tail=new_node
        self.count+=1
    
    def del_head(self):
        if self.count==0:
            print("No element")
        elif self.count==1:
            self.head=self.tail=None
            self.count-=1
        else:
            self.head=self.head.next
            self.count-=1

    def del_tail(self):
        if self.count==0:
            print("No element")
        elif self.count==1:
            self.head=self.tail=None
            self.count-=1
        else:
            temp=self.head
            while temp.next!=self.tail:
                temp=temp.next
            self.tail=temp
            self.count-=1

    def print_listH(self):
        if self.count==0:
            print("No ele")
        temp=self.head
        while temp.next!=None:
            print(temp.data," | ",end="")
            temp=temp.next
        print(temp.data)



abc = LinkedList_()
abc.insert_head(10)
abc.print_listH()
abc.insert_head(47)
abc.insert_head(7)
abc.insert_tail(0)
abc.del_head()
abc.del_head()
abc.print_listH()
abc.insert_head(49)
abc.insert_head(71)
abc.print_listH()
abc.del_tail()
abc.del_tail()
abc.print_listH()