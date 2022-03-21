r = sorted([int(input()) for _ in range(int(input()))],key = lambda x:-x)
print(max([r[-1-_]*(len(r)-_) for _ in range(len(r))]))
