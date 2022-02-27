t = input()
if t.count(":-)") + t.count(":-(") > 0:
    h,s = t.count(")"),t.count("(")
    if h == s:
        print("unsure")
    elif h > s:
        print("happy")
    else :
        print("sad")
else:
    print("none")
