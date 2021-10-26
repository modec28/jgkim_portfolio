a = []
for i in range(0,10):
    b=int(input())
    while(b<0 or b>1000):
        b = int(input())
    if a.count(b%42) == 0:
        a.append(b%42)
print(len(a))
