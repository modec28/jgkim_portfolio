a = list(input())
for i in range(int(input())):
    c1,c2 = map(int,input().split())
    c = a[c1]
    a[c1] = a[c2]
    a[c2] = c
print(*a,sep = "")
