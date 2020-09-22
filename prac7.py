t=['reading', 'study', 'newspaper', 'book']
l=[]
for i in t:
    for k in i:
        j=i.count(k)
        if j>1:
            l.append(i)
print(set(l))