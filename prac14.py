import random 
# l=[]
mysum=0
for i in range(1, 10):
    r=random.randint(100, 200)
    mysum += mysum+r
    # l.append(r)
# for i in l:
#     mysum += i


# mysum=sum(l)
print(mysum)