a = input()
c = ""
for i in list(map(int,input().split())):
    if i == 0:
        c += " "
    elif i<=26:
        c += chr(i+64)
    else:
        c += chr(i+70)
c = sorted(c)
b = sorted(list(input()))
if c == b:
    print("y")
else:
    print("n")
