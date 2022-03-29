n = int(input())
a = list(map(int,input().split()))
b = [0]*n
s = sorted(a)
c = 0
for i in s:
    x = a.index(i)
    a[x] = -1
    b[x]=c
    c += 1
for i in b:
    print(i, end=" ")
