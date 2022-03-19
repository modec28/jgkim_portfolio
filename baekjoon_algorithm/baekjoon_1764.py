n,m = map(int,input().split())
n_list = [input() for i in range(n)]
m_list = []
for i in range(m):
    a = input()
    if a in n_list:
        m_list.append(a)
m_list.sort()
print(len(m_list))
print(*m_list,sep="\n")
