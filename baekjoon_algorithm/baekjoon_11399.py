int(input())
p = sorted(map(int,input().split()))
time = 0
for i in range(len(p)):
    time += sum(p[0:i+1])
print(time)
