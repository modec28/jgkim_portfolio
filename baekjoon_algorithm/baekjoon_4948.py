max_num = 123456
prime_num = []
for i in range(2,max_num*2):
    check = 0
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        prime_num.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    print(len(set(range(n+1,n*2+1))&set(prime_num)))
