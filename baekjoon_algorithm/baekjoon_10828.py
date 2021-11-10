# push = append
# pop = pop
# size = len
# empty = if len == 0
# top = [-1]
import sys
input = sys.stdin.readline
stack = []
for _ in range(int(input())):
    n = input().split()
    if n[0] == "push" != -1:
        stack.append(n[-1])
        continue
    elif n[0] == "pop" :
        if len(stack) == 0:
            print(-1)
            continue
        a = stack.pop()
        print(a)
    elif n[0] == "size" :
        print(len(stack))
        continue
    elif n[0] == "empty":
        a = 0
        if len(stack) == 0:
            a = 1
        print(a)
        continue
    elif n[0] == "top" :
        a = -1
        if len(stack) != 0:
            a = stack[-1]
        print(a)
        continue
