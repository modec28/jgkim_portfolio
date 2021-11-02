import sys
n=[]
for _ in range(int(input())):
    n.append(int(sys.stdin.readline()))
text = ""
for i in sorted(n):
    text += str(i)+"\n"
sys.stdout.write(text)
