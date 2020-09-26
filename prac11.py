l=[123,435,674]
l2=[]
for i in l:
    n=str(i)
    l2.append(int(n[::-1]))
print(l2)