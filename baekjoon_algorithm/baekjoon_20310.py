n = input()
print(*[str(i)*(n.count(str(i))//2) for i in range(2)],sep = "")
