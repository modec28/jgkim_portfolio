a = input()
b = sorted([a[i:] for i in range(len(a))])
print(*b,sep = "\n")
