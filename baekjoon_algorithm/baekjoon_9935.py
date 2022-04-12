a = input()
b = input()
c = []
for i in a:
    c.append(i)
    if b[-1] == i and "".join(c[-len(b):])== b:
        del c[-len(b):]
print("".join(c)) if c else print("FRULA")
