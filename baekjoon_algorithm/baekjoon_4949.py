while True:
    n = input()
    k = []
    if n == ".":
        break
    for i in n:
        if i == "("or i == "[":
            k.append(i.replace("[","]").replace("(",")"))
        elif i == ")"or i == "]":
            if len(k) == 0:
                k.append("fail")
                break
            if k[-1] == i:
                del k[-1]
            else :
                break
    if len(k) == 0:
        print("yes")
    else:
        print("no")
