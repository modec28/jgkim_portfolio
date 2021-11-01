ALPHA = "22233344455566677778889999"
sum = 0
for i in list(input()):
    sum = sum + int(ALPHA[ord(i)-65])+1
print(sum)
