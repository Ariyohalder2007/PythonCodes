f=open('D:/python course codes/hw1.txt', 'w')
f.write('Ariyo Halder\nClass 7\n7')
f.close()
s=''
f=open('D:/python course codes/hw1.txt', 'r')
r=f.read()

print(r.split(' ', 1))
f.close()