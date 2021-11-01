while True:
    a = list(map(int,input().split()))
    if a.count(0) == len(a):
        break
    print(sum(a)) 
