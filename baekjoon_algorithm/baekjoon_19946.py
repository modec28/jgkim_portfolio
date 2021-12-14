n,s = int(input()),64
while True:
    if n % 2 != 0:
        break
    n //=2
    s -= 1
print(s)
