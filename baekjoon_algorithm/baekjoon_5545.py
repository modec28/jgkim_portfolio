n = int(input())
a,b = map(int,input().split())
c = int(input())
d = sorted([int(input()) for i in range(n)],reverse = True)
e = []
for i in range(1,len(d)+1):
    e.append(int((c+sum(d[0:i]))/(a+b*i)))
print(max(e))
