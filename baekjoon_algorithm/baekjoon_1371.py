c = [0] * 26
a = []
while True:
    try :
        t = input()
        a.extend(list(t))
    except :
        break
for i in range(0,26):
    c[i] = a.count(chr(ord("a")+i))
m = max(c)
for i in range(0,26):
    if m == c[i]:
        print(chr(ord("a")+i),end="")
