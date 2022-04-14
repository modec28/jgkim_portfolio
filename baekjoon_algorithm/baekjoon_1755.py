eng = ["zero","one","two","three","four","five","six","seven","eight","nine"]
a,b = map(int,input().split())
l = []
for i in range(a,b+1):
    t = "".join([eng[j] for j in list(map(int,str(i)))])
    l.append([t,i])
l.sort(key = lambda x:x[0])
c = 0
for i in l:
    c += 1
    print(i[1],end = " ") if c%10 != 0 else print(i[1])
