import sys
n=[0]*10001
for _ in range(int(input())):
    n[int(sys.stdin.readline())]+=1
for i in range(len(n)):
    if n[i] != 0:
        for j in range(n[i]):
            sys.stdout.write(str(i)+"\n")
