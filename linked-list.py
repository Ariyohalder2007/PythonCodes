class Node:
    def __init__(self, data=None):
        self.data=data
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None
    def display(self):
        printval=self.headval
        while printval is not None:
            print(printval.data)
            printval=printval.nextval
    def insertAtbeginning(self,newdata):
        newnode=Node(newdata)
        newnode.nextval=self.headval
        self.headval=newnode
   



s=SLinkedList()
s.headval=Node(3)
a=Node(4)
b=Node(5)
s.headval.nextval=a
a.nextval=b
s.insertAtbeginning(2)
s.display()