for i in range(0,int(input())):
    a, b = input().split()
    b = list(b)
    for j in b:
        print(j*int(a), end="")
    print()
