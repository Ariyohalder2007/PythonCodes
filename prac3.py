l=['Apple', 'Mango', 'Grape']

for i in l:
    # print(type(i))
    for j in i.lower():
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            print(j)
