while True:
    try:
        l,u,n,s = 0,0,0,0
        for i in input():
            if i == " ":
                s +=1
            elif i in "1234567890":
                n +=1
            else:
                if i.isupper() == True:
                    u+=1
                else :
                    l+=1
        print("%d %d %d %d"%(l,u,n,s))
    except:
        break
