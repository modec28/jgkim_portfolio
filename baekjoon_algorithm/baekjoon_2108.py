import sys
from collections import Counter

a = []

for _ in range(int(input())):
    a.append(int(sys.stdin.readline()))
a.sort()

c=Counter(a).most_common()
t = c[0][0]
if len(c)>1:
    if c[0][1] == c[1][1]:
        t = c[1][0]

print(round(sum(a)/len(a)))
print(a[int((len(a)-1)/2)])
print(t)
print(max(a)-min(a))
