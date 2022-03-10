a = []
for i in range(int(input())):
    s = list(input().split())
    s[1:]=map(int,(s[1],s[2],s[3]))
    a.append(s)
s = sorted(a, key = lambda x:(-x[1],x[2],-x[3],x[0]))
for i in s:
    print(i[0])
