l,s = [int(input()) for i in range(10)],[]
for i in range(10):
    c=sum(l)
    s.append([c,abs(c-100)])
    l.pop()
print(sorted(s,key = lambda x:(x[1],-x[0]))[0][0])
