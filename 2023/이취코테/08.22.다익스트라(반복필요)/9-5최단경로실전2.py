import sys
import heapq
n, m, start = map(int, input().split())

input = sys.stdin.readline
INF = int(1e9)

distance = [INF] * (n+1)

graph = [[] for i in range (n+1)]

for i in range (m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dij(start)

count = 0
max_dist = 0
for i in distance:
    if i != INF:
        count += 1
        max_dist = max(max_dist, i)

print(count-1, max_dist)