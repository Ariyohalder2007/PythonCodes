p={"a":"apple", "b":"ball", "c":"cat", "d":"dog"}
p1={"b":"ball", "c":"doog", "d":"dog"}
l=[]
k1=p.keys()
k2=p1.keys()
for i in k1:
    for j in k2:
        if i==j:
            l.append(i)
for i in l:
    if p.get(i)==p1.get(i):
        print(i,"valid")
    else:
        print(i,"invalid")