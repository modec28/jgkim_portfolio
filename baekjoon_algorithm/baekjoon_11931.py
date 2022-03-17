import sys
print(*sorted(int(sys.stdin.readline()) for i in range(int(input())))[::-1])
