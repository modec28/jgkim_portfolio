n,m = map(int,input().split())
c = []
for _ in range(n):
    c.append(list(map(int,input().replace("B","0").replace("W","1"))))
count_max = 0
for i in range(n-7):
    for j in range(m-7):
        count = 0
        for y in range(8):
            for x in range(8):
                if c[i+y][j+x] == (x+y)%2:
                    count += 1
        count_max = max(count,64-count,count_max)
print(64-count_max)
