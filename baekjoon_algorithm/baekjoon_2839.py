n = int(input())
if n % 5 == 0 :
    print(n//5)
else:
    c5 = n//5
    while True:
        r5 = n-c5*5
        if r5 % 3 == 0:
            print(r5//3 + c5)
            break
        c5 = c5-1
        if c5 < 0:
            print(-1)
            break
