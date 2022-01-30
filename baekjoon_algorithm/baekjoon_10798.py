a = []
try:
    while True:
        a.append(input())
except:
    b = 0
    d = ""
    while True:
        c = 0
        for i in range(len(a)):
            if len(a[i])<= b:
                continue
            d+=a[i][b]
            c += 1
        if c == 0 :
            break
        b += 1
    print(d)
