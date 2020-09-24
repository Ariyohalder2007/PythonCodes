l=[2,4,3,1,727]
l2=[]
for i in l:
    l2.append(i**2)
res=dict(zip(l, l2))
print(res)