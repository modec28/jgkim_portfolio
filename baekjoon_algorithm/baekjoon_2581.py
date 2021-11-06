prime = []
m=int(input())
n=int(input())
for i in range(m,n+1):
    check = 0
    if i == 1 :
        continue
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        prime.append(i)
if len(prime) > 0:
    print(sum(prime))
    print(min(prime))
else :
    print(-1)
