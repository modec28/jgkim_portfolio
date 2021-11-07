n = []
for i in range(int(input())):
    n.append(list(map(int,input().split())))
for i in n:
    rank_a = 1
    for j in n:
        if i == j:
            continue
        if i[0] < j[0] and i[1] < j[1]:
            rank_a += 1
    print(rank_a,end=" ")
