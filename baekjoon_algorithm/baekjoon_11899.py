t = input().replace("()","")
while t.count("()") != 0:
    t = t.replace("()","")
print(len(t))
