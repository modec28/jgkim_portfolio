import sys
n = []
for _ in range(int(input())):
    text = sys.stdin.readline()
    app = [len(text),text]
    if n.count(app)>0:
        continue
    n.append(app)
for i in sorted(n):
    sys.stdout.write(i[-1])
