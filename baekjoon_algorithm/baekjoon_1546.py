a = int(input())
b = list(map(int,input().split()))
m = max(b)
avr = 0
for i in range(0,a):
    b[i] = b[i]/m*100
    avr = avr + b[i]

print(avr/a)
