n = int(input())+10
sum = 1
i = 0
while True:
    sum = sum + i
    i += 1
    if n//6 <= sum:
        print(i)
        break
