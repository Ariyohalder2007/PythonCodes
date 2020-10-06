
class stack:
    def __init__(self):
       
        self.l=[]
    def show(self):

        print(self.l)
    def push(self, element):
        self.l.append(element)
    def remove(self, element):
        self.l.remove(element)
    def pop(self):
        return self.l.pop()
s=stack()
s.push(5)
s.push(5)
s.push(3)
s.push(5)
s.push(5)
s.push(2)
s.push(2)
s.push(2)
# s.remove(2)
s.pop()
s.show()
