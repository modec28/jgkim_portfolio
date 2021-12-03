n = int(input())
a = sorted(map(int,input().split()))
b = sorted(map(int,input().split()),reverse = True)
for i in range(n):
    a[i] *= b[i]
print(sum(a))
