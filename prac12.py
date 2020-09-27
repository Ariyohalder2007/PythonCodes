
l=[i for i in range(2, 20) if all(i%j!=0 for j in range(2, i))]
print(l)