n = []
for _ in range(int(input())):
    n.append(list(map(int,input().split())))
for i in sorted(n):
    print(*i)
