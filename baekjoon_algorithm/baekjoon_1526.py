n = int(input())
prt = 0
for i in range(n,3,-1):
    if len(str(i).replace("4","").replace("7","")) == 0:
        prt = i
        break
print(prt)
