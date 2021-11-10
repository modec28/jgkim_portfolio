import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
q = deque([i+1 for i in range(n)])
print("<",end = "")
while len(q)>1:
    for _ in range(k-1):
        q.append(q.popleft())
    print(q.popleft(),end=", ")
print(*q,end = ">")
