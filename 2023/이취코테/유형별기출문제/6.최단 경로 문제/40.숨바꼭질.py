import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))


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

dij(1)

dij_max = 0
for i in range(1, n+1):
    dij_max = max(dij_max, distance[i])

index = []
for i in range(1, n+1):
    if distance[i] == dij_max:
        index.append(i)

print(index[0], distance[index[0]], len(index))