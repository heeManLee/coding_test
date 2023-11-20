## https://school.programmers.co.kr/learn/courses/30/lessons/132266
## 다익스트라 좋은 예제.. 할 줄 알아야한다..

import heapq

INF = int(1e9)

def dij(start, distance, graph):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    
    for i in range(len(roads)):
        a, b = roads[i]
        graph[a].append((b, 1))
        graph[b].append((a,1))
    
    distance = dij(destination, distance, graph)
    
    for i in sources:
        if distance[i] == INF:
            answer.append(-1)
        else:
            answer.append(distance[i])
    
    
    return answer