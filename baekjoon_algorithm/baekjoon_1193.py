x = int(input())
n = 0
if x == 1:
    print("1/1")
elif x == 2:
    print("1/2")
for i in range(0,x):
    n += i
    if n>=x:
        m = i-(n-x)
        n = i+1-m
        if i % 2 == 0 :
            print("%d/%d"%(m,n))
            break
        else :
            print("%d/%d"%(n,m))
            break
