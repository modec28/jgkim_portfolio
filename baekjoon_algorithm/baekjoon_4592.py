while True:
    l = list(map(int,input().split()))
    s = []
    if l[0] == 0:
        break
    l.remove(l[0])
    for i in range(len(l)):
        if len(s) != 0:
            if l[i] == s[-1]:
                continue
        s.append(l[i])
    print(*s, end = " $")
    print()
