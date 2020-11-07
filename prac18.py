d1={'a':'apple', 'b':'bannana', 'c':'cat', 'd':'dog'}
d2={'a':'apple', 'b':'bannana', 'c':'cat'}
k1=d1.keys()
k2=d2.keys()
l=[]
for i in k1:
    for j in k2:
        if i==j:
            
            l.append(d1[i])
print(l)
