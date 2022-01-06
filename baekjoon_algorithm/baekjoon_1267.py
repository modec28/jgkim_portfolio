int(input())
n = list(map(int,input().split()))
y,m = 0,0
for i in n:
    y += ((i//30)+1)*10
    m += ((i//60)+1)*15
if y == m :
    print("Y M %d"%m)
elif y > m:
    print("M %d"%m)
else:
    print("Y %d"%y)
