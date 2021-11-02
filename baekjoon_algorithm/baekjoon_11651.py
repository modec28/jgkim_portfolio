n = []
for _ in range(int(input())):
    n.append(list(map(int,input().split()[::-1])))
for i in sorted(n):
    print(*i[::-1])
