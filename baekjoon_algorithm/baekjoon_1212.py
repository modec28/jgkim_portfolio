n = list(map(int,input()))
for i in range(len(n)):
    b = bin(n[i])[2:]
    if i != 0:
        for j in range(3-len(b)):
            b = "0"+b
    print(b,end = "")
