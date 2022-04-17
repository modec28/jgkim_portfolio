n = int(input())
a = n

if n>99:
    a = 99
    for i in range(100,n+1):
        if i == 1000:
            continue
        if (i//100 - i%100//10) == (i%100//10-i%10):
            a+=1
print(a)
