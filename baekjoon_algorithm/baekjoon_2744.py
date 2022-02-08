c = ""
for i in input():
    t = -32
    if ord(i) < 97:
        t = 32
    c += chr(ord(i)+t)
print(c)
