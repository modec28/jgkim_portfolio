from collections import Counter
print(sorted(Counter([int(input()) for i in range(int(input()))]).items(), key = lambda x:(-x[1],x[0]))[0][0])
