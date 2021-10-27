row = 8
col = 8
count = 0
for i in range(0,col):
    text=input()
    for j in range(0,row):
        if(i + j)%2 == 0 and text[j] == "F" :
            count = count + 1
print(count)
