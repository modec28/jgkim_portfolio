t = []
for i in range(int(input())):
    t.append(list(input()))
wrong = 0
for i in range(len(t)):
    for j in range(len(t[0])):
        if t[j][i] != t[i][j]:
            wrong = 1
            break
    if wrong == 1:
        break
if wrong == 0:
    print("YES")
else:
    print("NO")
