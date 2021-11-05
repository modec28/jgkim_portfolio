def era(n):
    if n < 2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return n
def gold(n):
    for i in range(n//2,1,-1):
        if era(i) * era(n-i) !=0:
            return [i, n-i]

for _ in range(int(input())):
    print(*gold(int(input())))
