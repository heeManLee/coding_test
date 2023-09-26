# https://school.programmers.co.kr/learn/courses/30/lessons/72413?language=python3
## 폴로이드를 실전에서 쓸 수 있도록 반드시 연습해 놓을것, 양갈레 생각 할 것

INF = int(1e9)

def solution(n, s, a, b, fares):
    answer = INF
    
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
                
    for i in range(len(fares)):
        graph[fares[i][0]][fares[i][1]] = fares[i][2]
        graph[fares[i][1]][fares[i][0]] = fares[i][2]
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for i in range(1, n+1):
        answer = min(graph[s][i] + graph[i][a] + graph[i][b], answer)
    
    return answer