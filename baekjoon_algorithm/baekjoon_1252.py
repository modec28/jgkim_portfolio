b1,b2 =input().split()
b1 = int("0b"+b1,2)
b2 = int("0b"+b2,2)
print(bin(b1+b2)[2:])
