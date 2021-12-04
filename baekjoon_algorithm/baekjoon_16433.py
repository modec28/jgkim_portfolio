n,r,c = map(int,input().split())
a = [[(i+j)%2 for j in range(n)]for i in range(n)]
no = "."
yes = "v"
if a[c-1][r-1] != 1:
    no = "v"
    yes = "."
for i in a:
    for j in i:
        print(str(j).replace("0",no).replace("1",yes), end = "", sep ="")
    print()
