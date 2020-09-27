d={'a':2, 'b':5, 'c':10}

count=0

for k, i in d.items():
    for j in range(2,i):
        if i%j==0:
            count=1
            break
        else:
            count = 0
    if count==0:
        print(k, i)
