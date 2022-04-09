import heapq
t = [tuple(map(int,input().split())) for _ in range(int(input()))]
h = [0]
for i in sorted(t):
    if h[0]<= i[0]:
        heapq.heappop(h)
    heapq.heappush(h, i[1])
print(len(h))
