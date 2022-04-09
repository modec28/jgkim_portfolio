n = int(input())
a = list(map(int, input().split()))
x = int(input())
c = 0
a.sort()
l, r = 0, n-1
while l < r:
    s = a[l] + a[r]
    if s < x:
        l += 1
    elif s > x:
        r -= 1
    else:
        c += 1
        l += 1
print(c)
