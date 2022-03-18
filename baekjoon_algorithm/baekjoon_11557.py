for i in range(int(input())):
    d = []
    for j in range(int(input())):
        a = input().split()
        a[1] = int(a[1])
        d.append(a)
    d.sort(key = lambda x:-x[1])
    print(d[0][0])
