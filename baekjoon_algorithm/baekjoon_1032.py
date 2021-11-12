t = []
n = int(input())
for _ in range(n):
    t.append(list(input()))
for _ in range(len(t[0])):
    for i in range(1,n):
        if t[i][_] != t[0][_]:
            t[0][_] = "?"
print(*t[0],sep="")
