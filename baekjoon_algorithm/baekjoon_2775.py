for _ in range(int(input())):
    k = int(input())
    n = int(input())
    p = [i+1 for i in range(n)]
    for i in range(k):
        q = [0]*n
        for j in range(n):
            q[j] = sum(p[:j+1])
        p = q
    print(p[n-1])
