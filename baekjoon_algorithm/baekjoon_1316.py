count = int(input())
for i in range(0,count):
    a = input()
    now = 0
    c = [0]*26
    for j in a:
        s = ord(j)-97
        if now != s:
            if c[s] == 1:
                count = count - 1
                break
            now = s
            c[s] = 1
        else :
            c[s] = 1
print(count)
