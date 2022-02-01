sum = 0
lc = ""
for i in input():
    if lc != i:
        sum+=10
        lc = i
        continue
    sum+=5
print(sum)
