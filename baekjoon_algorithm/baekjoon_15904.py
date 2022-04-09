a = input()
b = list("UCPC")
c = "I hate UCPC"
for i in a:
    if b[0] == i:
        b.pop(0)
    if len(b) == 0:
        c = "I love UCPC"
        break
print(c)
