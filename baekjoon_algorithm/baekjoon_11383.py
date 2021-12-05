n,m = map(int,input().split())
a_list = []
b_list = []
for i in range(n):
    a_list.append(input())
for i in range(n):
    b_list.append(input())
for i in range(n):
    skip = 0
    text = ""
    for j in a_list[i]:
        text += j*2
    if text != b_list[i]:
        skip = 1
        print("Not Eyfa")
        break
if skip == 0:
    print("Eyfa")
