import sys
f = sorted([float(sys.stdin.readline()) for i in range(int(input()))])
for i in range(7):
    print("%.3f" %f[i])
