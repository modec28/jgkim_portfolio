import sys
sys.setrecursionlimit(10000)

T = int(input())

def dfs(x,y):
    if 0 <= x < n and 0 <= y < m:
        if g[x][y] == 1:
            g[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return 1
    return 0

for i in range(T):
    m,n,k = map(int, input().split())

    g = [[0]*m for _ in range(n)]

    for i in range(k):
        a, b= map(int, input().split())
        g[b][a] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if dfs(i,j) == 1:
                count += 1
    print(count)
