import sys
import heapq

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

INF = int(1e9)

for i in range(m):
    x, y, c = map(int, input().split())
    graph[x].append((y, c))

distance = [INF] * (n+1)

def dij(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dij(start)

answer = 0
count = 0
for i in range(1, len(distance)):
    if distance[i] == 0 or distance[i] == INF:
        continue
    answer += 1
    count = max(count, distance[i])

print(answer, count)