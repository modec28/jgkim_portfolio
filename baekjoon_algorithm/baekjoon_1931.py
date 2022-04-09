time,c,b = sorted([list(map(int,input().split())) for i in range(int(input()))],key = lambda x:(x[1],x[0])),0,0
for i in time:
    if i[0]>=b:
        c+=1
        b=i[1]
print(c)
