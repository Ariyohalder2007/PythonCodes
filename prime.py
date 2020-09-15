a=17
for i in range(1, a):

    if a%i==0:
        count=0
        break
    else:
        count=1

if count!=0:
    print('prime')
else:
    print('not prime')