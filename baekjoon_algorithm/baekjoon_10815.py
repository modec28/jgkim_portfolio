a = input()
a = set(map(int,input().split()))
b = input()
print(*[1 if i in a else 0 for i in map(int,input().split())])
