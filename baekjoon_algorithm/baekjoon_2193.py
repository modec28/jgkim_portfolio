a=int(input())
d=[1,1]
for i in range(2,a):
    d.append(d[i-1]+d[i-2])
print(d[a-1])
