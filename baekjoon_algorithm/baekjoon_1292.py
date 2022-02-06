n = []
for i in range(46):
    n+= [i]*i
a,b = map(int,input().split())
print(sum(n[a-1:b]))
