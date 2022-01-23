t = ['a', 'e', 'i', 'o', 'u']
while True:
    c = 0
    a = input().lower()
    if a == "#":
        break
    for i in t:
        if i in a:
            c += a.count(i)
    print(c)
