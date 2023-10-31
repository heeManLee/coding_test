import sys
from collections import deque
input = sys.stdin.readline

graph = []
answer = 100000000
n,m = map(int, input().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(int, input().split())))

virus = []
goal = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i,j])
        elif graph[i][j] == 0:
            goal += 1
            

active = [0] * len(virus)

def infect():
    global goal
    temp_time = 0
    temp_result_time = 0
    count = 0

    q = deque()
    visited = [[0] * n for _ in range(n)]
    for i in range(len(active)):
        if active[i] == 1:
            q.append([virus[i][0], virus[i][1], 0])
            visited[virus[i][0]][virus[i][1]] = 1

    while q:
        y, x, temp_time = q.popleft()
        if count == goal:
            return temp_result_time

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n or graph[ny][nx] == 1 or visited[ny][nx] == 1:
                continue
            
            q.append([ny, nx, temp_time + 1])
            visited[ny][nx] = 1
            temp_result_time = temp_time + 1
            if graph[ny][nx] == 0:
                count += 1

    return 100000000




def go(idx):
    global m
    global answer
    if sum(active) == m:
        answer = min(answer, infect())
        return

    for i in range(idx, len(active)):
        active[i] = 1
        go(i+1)
        active[i] = 0

go(0)

if answer == 100000000:
    print(-1)
else:
    print(answer)
