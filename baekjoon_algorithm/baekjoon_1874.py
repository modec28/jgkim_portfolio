import sys
input = sys.stdin.readline

j = 1
fail = 0
stack = []
prt = ""
n = int(input())
for _ in range(n):
    a = int(input())
    if fail == 0:
        while True:
            if len(stack) > 0:
                if stack[-1] == a:
                    prt += "-\n"
                    del stack[-1]
                    break
                if stack[-1] > a:
                    fail = 1
                    prt = "NO"
                    break
            stack.append(j)
            prt += "+\n"
            if j < n+1:
                j += 1
print(prt)
