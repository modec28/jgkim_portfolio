a,b,c = map(int,input().split())
m = 0
if a*b*c != 0and c-b != 0:
    m = a//(c-b)+1
if m <= 0 :
    m = -1
print(m)
