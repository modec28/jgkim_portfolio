sum = 1
for i in range(0,3):
    b= int(input())
    sum *= b
strsum = list(str(sum))
for i in range(0,10):
    print(strsum.count(str(i)))
