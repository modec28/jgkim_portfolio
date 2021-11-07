n = input()
if len(n) < 2:
    n = "0"+n
s = list(map(int,n))
n = list(map(int,n))
step = 0
while True:
    step += 1
    a = sum(n)
    n[0] = n[1]
    n[1] = a%10
    if n[0]==s[0] and n[1]==s[1]:
        print(step)
        break
