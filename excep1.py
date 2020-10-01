s="hello"
try:
    print(s[7])
except IndexError:
    print('invalid range')