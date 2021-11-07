import sys
n=int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
s = sorted(list(set(x)))
d = {v: i for i, v in enumerate(s)}
print(*[d[i] for i in x])
