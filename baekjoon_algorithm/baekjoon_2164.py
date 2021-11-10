import sys
from collections import deque
input = sys.stdin.readline
q = deque([i+1 for i in range(int(input()))])
while len(q)>1 :
    q.popleft()
    q.append(q.popleft())
print(*q)
