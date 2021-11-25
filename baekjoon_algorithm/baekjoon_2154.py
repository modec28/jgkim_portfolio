n = int(input())
text = ""
for i in range(n):
    text += str(i+1)
print(text.find(str(n))+1)
