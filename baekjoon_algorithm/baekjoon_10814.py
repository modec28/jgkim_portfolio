import sys
n = []
for i in range(int(input())):
    a,b = sys.stdin.readline().split()
    text = [int(a),i,b]
    n.append(text)
for i in sorted(n):
    sys.stdout.write(str(i[0])+" "+i[-1]+"\n")
