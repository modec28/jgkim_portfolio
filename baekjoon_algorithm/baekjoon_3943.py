import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    max_int = n
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3 + 1
        if n > max_int:
            max_int = n
    print(max_int)
