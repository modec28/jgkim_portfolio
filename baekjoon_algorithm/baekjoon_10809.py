a = list(input())
for i in range(ord('a'),ord('z')+1):
    b = -1
    for j in a:
        if a[j] == chr(i) and b == -1:
            b = j
            break
    print(b)
