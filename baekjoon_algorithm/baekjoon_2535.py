a = sorted([list(map(int,input().split())) for i in range(int(input()))],key = lambda x:-x[2])
while a[2][0] == a[0][0]:
    del a[2]
print(*a[0][0:2])
print(*a[1][0:2])
print(*a[2][0:2])
