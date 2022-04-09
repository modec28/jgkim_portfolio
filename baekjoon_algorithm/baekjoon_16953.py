a,b=map(int,input().split())
c = 1
while b != a:
    if a==b :
        break
    if a>b :
        c = -1
        break
    if b%2==0:
        b = b//2
    else:
        if b%10 == 1:
            b = b//10
        else:
            c = -1
            break
    c += 1
print(c)
