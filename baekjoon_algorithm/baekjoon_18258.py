import sys
from collections import deque
input = sys.stdin.readline
stack = deque()
for _ in range(int(input())):
    n = input().split()
    a = 0
    if n[0] == "push" != -1:
        stack.append(n[-1])
        continue
    elif n[0] == "pop" :
        if len(stack) == 0:
            print(-1)
            continue
        a = stack.popleft()
    elif n[0] == "size" :
        a = len(stack)
    elif n[0] == "empty":
        a = 0
        if len(stack) == 0:
            a = 1
    elif n[0] == "front" :
        a = -1
        if len(stack) != 0:
            a = stack[0]
    elif n[0] == "back" :
        a = -1
        if len(stack) != 0:
            a = stack[-1]
    print(a)
