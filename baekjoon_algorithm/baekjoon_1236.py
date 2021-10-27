a, b = map(int,input().split())
c = [0 for i in range(b)]
d = []
for i in range(0,a):
    t = list(input())
    if t.count("X") > 0:
        for j in range(0,len(t)):
            if t[j] == "X":
                c[j] = 1
    else :
        d.append(t)
e = len(c)-c.count(1)
if len(d) > e:
    e = len(d)
print(e)
