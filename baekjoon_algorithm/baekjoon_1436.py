a = []
n = 665
while True:
    n += 1
    if str(n).count("666")>0:
        a.append(n)
    if len(a) > 9999:
        break
print(a[int(input())])
