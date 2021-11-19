n = input()
n = int(n[0:len(n)-2]+"00")
f = int(input())
for _ in range(0,100):
    if (n+_)%f == 0:
        if _ < 10 :
            print("0",_,sep = "")
            break
        print(_)
        break
