a,t = input(),""
for i in a:
    if ord(i) in range(65,91):
        i = chr((ord(i)-52)%26+65)
    elif ord(i) in range(97,123):
        i = chr((ord(i)-84)%26+97)
    t+=i
print(t)
