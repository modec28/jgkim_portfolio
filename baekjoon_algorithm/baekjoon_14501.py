import sys

N = int(input())

t = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

dp = [0 for i in range(N+1)]

for i in range(N-1,-1,-1):
    if i + t[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(t[i][1] + dp[i + t[i][0]], dp[i+1])

print(dp[0])
