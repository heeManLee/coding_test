# https://school.programmers.co.kr/learn/courses/30/lessons/118669
## 다익스트라를 응용하는 좋은 문제

## 아쉬운점 : 다익스트라 결과로 나오는 의미가 무엇인지 정확히 알아야 할 것 같다..
##           기본적으로 아직 너무 부족함

import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    answer = []
    
    summits.sort()
    summits_set = set(summits)
    
    graph = defaultdict(list)
    for i, j, cost in paths:
        graph[i].append((cost, j))
        graph[j].append((cost, i))
        
    def get_min_intensity():
        pq = []
        visited = [100000001] * (n+1)
        
        for gate in gates:
            heapq.heappush(pq, (0, gate))
            visited[gate] = 0
        
        while pq:
            intensity, node = heapq.heappop(pq)
            
            if node in summits_set or intensity > visited[node]:
                continue
            
            for weight, next_node in graph[node]:
                new_intensity = max(intensity, weight)
                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heapq.heappush(pq, (new_intensity, next_node))
        
        min_intensity = [0, 100000001]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]
        
        return min_intensity
    
    
    
    return get_min_intensity()