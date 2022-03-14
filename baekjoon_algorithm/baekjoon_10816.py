from collections import Counter
a = input()
a = list(map(int,input().split()))
s = set(a)
c = Counter(a)
b = input()
print(*[c[i] if i in s else 0 for i in map(int,input().split())])
