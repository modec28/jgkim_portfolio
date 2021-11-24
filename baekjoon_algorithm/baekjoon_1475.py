import math
n = input().replace("9","6")
count_n = []
for i in sorted(set(n)):
    count_n.append(n.count(i))
    if i == "6":
        count_n[-1] = math.ceil(count_n[-1]/2)
print(max(count_n))
