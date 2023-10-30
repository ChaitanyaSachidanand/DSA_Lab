class LinkedList_():

    class Node():
        def __init__(self,data):
            self.data = data
            self.Llink =None
            self.Rlink =None

    def __init__(self):
        self.head = None
        self.head.Llink =None
        self.head.Rlink =None
        self.tail = None
        self.count = 0

    def is_Empty(self):
        if self.count == 0:
            return True
        else:
            return self.count

    def inset_head(self,element):
        new_node = self.Node(element)
        # if self.count!=0:
        link = self.head.Rlink
        self.head.Rlink = new_node
        new_node.Rlink = link
        new_node.Llink = self.head
        self.count+=1


    def insert_tail(self,element):
        new_node = self.Node(element)
        link = self.tail


            






    