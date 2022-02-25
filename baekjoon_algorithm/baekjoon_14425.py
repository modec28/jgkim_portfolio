s,count = [],0
a ,b = map(int,input().split())
s = set([input() for _ in range(a)])
for i in range(b):
    t = input()
    if t in s:
        count +=1
print(count)
