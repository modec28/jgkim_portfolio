n = int(input())
w = sorted(map(int,input().split()))
t=1
for i in w:
    if t<i:
        break
    t+=i
print(t)
