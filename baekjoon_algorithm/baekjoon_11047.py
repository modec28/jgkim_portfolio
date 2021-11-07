n,k = map(int,input().split())
a = []
count = 0
for _ in range(n):
    a.append(int(input()))
for i in a[::-1]:
    if k // i > 0 :
        count += k // i
        k -= (k // i)*i
print(count)
