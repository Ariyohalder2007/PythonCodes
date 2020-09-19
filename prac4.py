x1={'Apple', 'Human', 'Flower'}
x2={'Apple', 'Internet', 'Pizza'}

y=x1 & x2
# print(type(y))
# list(y)
count=0
for i in y:
    for j in i:
        z=i.count(j)
        if z>1:
            print(j, z)
