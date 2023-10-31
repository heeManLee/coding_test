## https://school.programmers.co.kr/learn/courses/30/lessons/49191
## 아쉬운 점 : 이기는 그래프와 지는 그래프를 따로 나눠서 생각해야 했다,
##             플로이드 워셜로 풀었어야했다.

def solution(n, results):
    answer = 0
    
    INF = int(1e9)
    win_graph = [[INF] * (n+1) for _ in range(n+1)]
    lose_graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for a in range(1,n+1):
        for b in range(1, n+1):
            if a == b:
                win_graph[a][b] = 0
                

    for i in range(len(results)):
        a, b = results[i]
        win_graph[a][b] = 1
        lose_graph[b][a] = -1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                win_graph[i][j] = min(win_graph[i][j], win_graph[i][k] + win_graph[k][j])

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                lose_graph[i][j] = min(lose_graph[i][j], lose_graph[i][k] + lose_graph[k][j])

    result_graph = [[INF] * (n+1) for _ in range(n+1)]
    for a in range(1,n+1):
        for b in range(1, n+1):
            result_graph[a][b] = min(result_graph[a][b], win_graph[a][b], lose_graph[a][b])
    
    for a in range(1, n+1):
        flag = 1
        for b in range(1,n+1):
            if result_graph[a][b] > int(1e6):
                flag = 0
                break

        if flag:
            answer +=1

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])