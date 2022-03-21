while True:
    n = int(input())
    if n == 0:
        break
    nn = []
    for i in range(n):
        a = input()
        nn.append([a,a.lower()])
    print(sorted(nn, key = lambda x:x[1])[0][0])
