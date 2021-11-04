n,m = map(int,input().split())
n = list(map(int,input().split()))
max = 0
for i in range(len(n)-2):
    for j in range(i+1,len(n)-1):
        for k in range(j+1,len(n)):
            s = sum([n[i],n[j],n[k]])
            if m - s >= 0:
                if m-max> m-s:
                    max = s
print(max)
