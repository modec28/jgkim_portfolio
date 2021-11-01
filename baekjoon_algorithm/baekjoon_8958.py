for _ in range(int(input())):
    ox = input()
    count = 1
    score = 0
    for i in range(len(ox)):
        if ox[i] == "X":
            count = 1
            continue
        if score != 0:
            if ox[i-1] == ox[i]:
                count = count+1
        score = score + count
    print(score)
