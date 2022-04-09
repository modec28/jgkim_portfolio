import sys
for i in range(int(input())):
    n = int(input())
    l = sorted([list(map(int,sys.stdin.readline().strip().split())) for i in range(n)], key = lambda x:x[0])
    c = 1
    m = l[0][1]
    for j in range(1,n):
        if l[j][1] < m:
            m = l[j][1]
            c +=1
    print(c)
