t = input()
c = 0
for i in range(len(t)-1):
    if t[i] != t[i+1]:
        c += 1
print(c//2 + c%2)
