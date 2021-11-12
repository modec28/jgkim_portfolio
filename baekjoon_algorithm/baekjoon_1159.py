m = ""
n = ""
for i in range(int(input())):
    n+=input()[0]
for i in range(0,26):
    if n.count(chr(ord("a")+i))>=5:
        m+=chr(ord("a")+i)
if len(m) == 0:
    m = "PREDAJA"
print(m)
