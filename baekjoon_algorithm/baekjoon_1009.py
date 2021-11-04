import sys
for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    c = pow(a,b,10)
    if c == 0:
        c = 10
    print(c)
