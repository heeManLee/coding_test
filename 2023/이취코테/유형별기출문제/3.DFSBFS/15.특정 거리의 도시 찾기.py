import heapq
import sys
INF = int(1e9)

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def djk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

djk(x)

count = []

for i in range(len(distance)):
    if distance[i] == k:
        count.append(i)

if len(count) == 0:
    print(-1)
else:
    count.sort()
    for i in count:
        print(i)
