prime = 0
input()
n = list(map(int,input().split()))
for i in n:
    check = 0
    if i == 1 :
        continue
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        prime = prime+1
print(prime)
