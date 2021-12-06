n = int(input())
c = 0
while n > 0:
    for i in range(1,n+1):
        if n < i :
            break
        n -= i
        c += 1
print(c)
