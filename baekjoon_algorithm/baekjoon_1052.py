def bottle(bot):
    global sum
    b = bin(bot)[2:]
    c = b.count("1")
    d = b[::-1]
    if c>k:
        for i in range(len(d)):
            if d[i] == "1":
                sum = sum+2**i
                return bottle(bot+2**i)
    return sum

sum = 0
n, k = map(int,input().split())
print(bottle(n))
