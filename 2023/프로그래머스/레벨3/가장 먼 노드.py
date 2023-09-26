## https://school.programmers.co.kr/learn/courses/30/lessons/49189
## 아쉬운점 : 다익스트라를 보면 겁부터 먹는다.. 최단 거리를 구하는 중요한 알고리즘이므로 반드시 알아야 한다.


import sys
import heapq

INF = int(1e9)

def solution(n, edge):
    answer = 0
    
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)
    
    for i in range(len(edge)):
        graph[edge[i][0]].append((edge[i][1], 1))
        graph[edge[i][1]].append((edge[i][0], 1))
    
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
    max_dist = -1
    for i in range(1, len(distance)):
        if distance[i] == INF:
            continue
        else:
            max_dist = max(max_dist, distance[i])
    
    for i in range(1, len(distance)):
        if distance[i] == max_dist:
            answer += 1
    
    return answer