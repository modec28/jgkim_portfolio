t = []
c = []
for i in range(5):
    t.append(input())
for i in range(len(t)):
    if "FBI" in t[i]:
        c.append(i+1)
if len(c) == 0:
    print("HE GOT AWAY!")
else:
    print(*c)
