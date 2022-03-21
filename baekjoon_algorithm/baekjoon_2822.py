s = sorted([[i+1,int(input())] for i in range(8)], key = lambda x:-x[1])[0:5]
print(sum([s[i][1] for i in range(5)]))
s= sorted(s,key = lambda x:x[0])
print(*[s[i][0] for i in range(5)])
