a, b = map(int,input().split())
n=min(a,b)
while True:
    if a%n ==0 and b%n==0:
        break
    n-=1

print(n)
print(int(a*b/n))
