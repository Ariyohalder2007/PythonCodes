l=[532, 123, 425]
msum=0
for i in l:
    msum=0
    for j in str(i):
        msum+=int(j)
    print(msum, end=" ")
