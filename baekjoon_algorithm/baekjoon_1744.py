import sys, collections
input = sys.stdin.readline

def solution(arr):
    ans = 0
    o, n, p = 0, [], []
    for i in arr:
        if i == 1:
            o += 1
        elif i > 1:
            p.append(i)
        else:
            n.append(i)
    n.sort(reverse=True)
    p.sort()
    while len(n) >= 2:
        a = n.pop()
        b = n.pop()
        ans += a*b
    while len(p) >= 2:
        a = p.pop()
        b = p.pop()
        ans += a * b
    if n: ans += n.pop()
    if p: ans += p.pop()
    return ans + o

N = int(input())
num = [int(input().rstrip()) for _ in range(N)]
print(solution(num))
