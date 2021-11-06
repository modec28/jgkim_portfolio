max_num = 10000
def check_selfnum(n):
    if n >= max_num:
        return 0
    sum = n + sum(map(int,list(str(n))))
    if selfnum.count(sum)>0:
        selfnum.remove(sum)
    else:
        return 0
    return check_selfnum(sum)

selfnum = list(range(1,max_num))
while True:
    if len(selfnum)>0:
        a = selfnum[0]
        check_selfnum(a)
        print(a)
        selfnum.remove(a)
    else:
        break
