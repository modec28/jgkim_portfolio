k = []
for _ in range(int(input())):
    n = int(input())
    if n == 0 :
        del k[-1]
    else:
        k.append(n)
print(sum(k))
