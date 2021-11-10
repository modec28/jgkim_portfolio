import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
stack = []
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        a[stack.pop()] = a[i]
    stack.append(i)
while stack:
    a[stack.pop()] = -1
print(*a,end=" ")
