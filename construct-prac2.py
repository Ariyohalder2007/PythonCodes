class shape:
    def __init__(self, l, b):
        self.l=l
        self.b=b
class rectangle(shape):
    def __init__(self, l, b):
        super().__init__(l, b)
    def area(self):
        print(self.l*self.b)


r=rectangle(20, 30)
r.area()