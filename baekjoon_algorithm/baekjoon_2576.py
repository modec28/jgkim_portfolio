h = []
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        h.append(n)
if len(h) != 0:
    print(sum(h))
    print(min(h))
else :
    print(-1)
