def generator(n):
    a, b = 0, 1

    while a < n:
        yield a
        a, b = b, a + b


a = generator(10)
for i in a:
    print(i, end=" ")
