f=open('D:/python course codes/prac5.txt', 'w')
f.write('Ariyo Halder Chowdhury')
f.close()

f=open('D:/python course codes/prac5.txt', 'r')
r=f.read()
print(r[0], end=" ")
for i in range(0, len(r)-1):
    if r[i]==' ':
        print(r[i+1], end=' ')
# r1=r.split(' ')
# print(r1[0][0], r1[1][0])
f.close()
