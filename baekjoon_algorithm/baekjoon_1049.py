n,m = map(int,input().split())
price_pkg = 1000
price_ea = 1000
price = 0
for _ in range(m):
    pkg, ea = map(int,input().split())
    price_pkg = min(pkg,price_pkg)
    price_ea = min(ea,price_ea)
while n :
    if n < 6:
        if price_pkg < price_ea*n:
            price += price_pkg
            break
        price += n*price_ea
        break
    if price_pkg < price_ea*6:
        price += price_pkg*(n//6)
        n -= (n//6)*6
        continue
    price += n*price_ea
    break
print(price)
