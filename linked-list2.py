class Node:
    def __init__(self, dataval=None):
        self.dataval=dataval
        self.nextval=None
class LinkedList:
    def __init__(self):
        self.headval=None
    def display(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
        def atBeginning(self, newdata):
            newnode=Node(newdata)
            newnode.nextval=self.headval
            self.headvalclass=newnode
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None
    def print_list(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def atbegin(self,newdata):
        newnode=Node(newdata)
        newnode.nextval=self.headval
        self.headval=newnode

l=SLinkedList()
l.headval=Node(1)
a=Node(2)
b=Node(3)
l.headval.nextval=a
a.nextval=b

l.atbegin(0)
l.print_list()
