a = input()
print(int(a,16)) if "x" in a else print(int(a,8)) if a[0] == "0" else print(int(a))
