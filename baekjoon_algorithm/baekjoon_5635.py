a = []
for i in range(int(input())):
    n = input().split()
    a.append([n[0],int(n[3]+(n[2] if(len(n[2]) == 2) else "0"+n[2])+(n[1] if(len(n[1]) == 2) else "0"+n[1]))])
a.sort(key = lambda x:x[1])
print(a[-1][0]+"\n"+a[0][0])
