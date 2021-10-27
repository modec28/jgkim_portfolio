cal = ["c=","c-","dz=","d-","lj","nj","s=","z="]
a = input()
for i in range(0,len(cal)):
    a = a.replace(cal[i],"0")
print(len(a))
