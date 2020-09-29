f=open('D:/test.txt', 'w')
f.write('Hello this is a test program')
f.close()

f=open('D:/test.txt', 'r')
print(f.read())