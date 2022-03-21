l = []
n = int(input())
for i in range(n):
    s = input()
    skip = 0
    for j in range(len(l)):
        if s in l[j] :
            l[j][1]-=1
            skip = 1
            break
    if skip == 1:
        continue
    l.append([s,n])
print(sorted(l, key = lambda x:(x[1],x[0]))[0][0])
