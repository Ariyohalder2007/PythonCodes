def MySort(mlist):
    n=len(mlist)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if mlist[j] > mlist[j+1]:
                mlist[j], mlist[j+1] = mlist[j+1], mlist[j]
    return mlist



l=[2, 66, 1, 0, 9, 10, 2, 3, 5]
print(MySort(l))