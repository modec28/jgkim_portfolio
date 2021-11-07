num = int(input())
tap = 0
for i in range(num):
    if 3**i == num:
        tap = i
        break

def star(n):
    if tap > n:
        global a
        a_len = len(a)
        a = a*3
        for x in range(len(a)):
            if(x//(len(a)//3) == 1):
                t = a[x]
                a[x]=t+[0]*len(t)+t
            else:
                a[x]=a[x]*3
        star(n+1)
    else:
        return

a = [[1,1,1],[1,0,1],[1,1,1]]
star(1)

for i in range(num):
    for j in range(num):
        c = " "
        if a[i][j] == 1:
            c = "*"
        print(c,end="")
    print("")
