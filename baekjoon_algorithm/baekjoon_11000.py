import heapq

n = int(input())
ca = [tuple(map(int,input().split())) for _ in range(n)]
ca.sort(key = lambda x:x[0])

heap = []
heapq.heappush(heap, ca[0][1])

for i in range(1,n):
    last = heapq.heappop(heap)
    if last > ca[i][0]:
        heapq.heappush(heap, last)
    heapq.heappush(heap, ca[i][1])

print(len(heap))
