h,m = map(int,input().split())
m+=int(input())
if m//60 >0:
    h+=m//60
print(h%24,m%60)
