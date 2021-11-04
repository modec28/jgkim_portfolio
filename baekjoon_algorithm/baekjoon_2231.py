n = int(input())
a = 0
for i in range(n):
    if n == i+sum(list(map(int,str(i)))):
        a = i
        break
print(a)
