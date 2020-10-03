class student:
    def __init__(self, n, s, r):
       self.n=n
       self.s=s
       self.r=r
    def detail(self):
        print(self.n, self.r, self.s)
s=student('Ariyo', 'Class7', '7')
s.detail()

