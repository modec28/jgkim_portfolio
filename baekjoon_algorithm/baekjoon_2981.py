import sys
n = int(sys.stdin.readline())
a = sorted([int(sys.stdin.readline()) for i in range(n)])

def gcd(n1, n2):
    while n2 :
        n1, n2 = n2, n1 % n2
    return n1

g = a[1] - a[0]

for i in range(2, n):
    g = gcd(g, a[i] - a[i-1])

s = [g]
for i in range(2, int(g**0.5)+1):
	if g % i == 0:
		print(i, end=' ')
		if i != g//i:
			s.insert(0, g//i)
print(*s)
