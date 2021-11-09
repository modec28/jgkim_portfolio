k = []
for _ in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        if i == "(":
            sum += 1
        if i == ")":
            sum -= 1
        if sum < 0:
            break
    if sum == 0 :
        print("YES")
    else :
        print("NO")
