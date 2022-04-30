def perm(n):
    if n == 2:
        if sum(s) == r:
            for i in s:
                h.remove(i)
            return 1
        return 0
    if sum(s) > r:
        return 0
    for i in range(9):
        if not c[i]:
            s[n] = h[i]
            c[i] = 1
            if perm(n + 1): return 1
            s[n] = 0
            c[i] = 0

h = [int(input()) for _ in range(9)]
r = sum(h) - 100
c = [0] * 9
s = [0] * 2
perm(0)
h.sort()
for i in h:
    print(i)
