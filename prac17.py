l=['12345', 2345, 9876, 'hi', 'kithelloe', '3452']
l2=[]

for i in l:
    try:
        l2.append(int(i))
    except Exception as e:
        # print(e)
        pass
print(l2)