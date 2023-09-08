from collections import deque
import copy
import sys

input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visit = [[0] * n for _ in range(n)]

shark_size = 2
shark_eat = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

fish = []
result = 0
q = deque()
for i in range(n):
    for j in range(n):
        if 1 <= graph[i][j] and graph[i][j] <= 6:
            fish.append((i,j,graph[i][j]))
        
        if graph[i][j] == 9:
            graph[i][j] = 0
            starty = i
            startx = j

def find_visit(f_y, f_x):
    global n
    global shark_size
    temp_visit = [[0] * n for _ in range(n)]
    while q:
        y, x, dist = q.popleft()
        temp_visit[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if ny == f_y and nx == f_x:
                return 1, dist+1
            
            if graph[ny][nx] <= shark_size and temp_visit[ny][nx] == 0:
                temp_visit[ny][nx] = 1
                q.append((ny, nx, dist+1))

    
    return 0, 0


while(1):
    can_eat = []
    for i in range(len(fish)):       
        if fish[i][2] < shark_size:
            q = deque()
            q.append((starty,startx, 0))
            can_visit, dist = find_visit(fish[i][0], fish[i][1])
            if can_visit:
                can_eat.append((dist, fish[i][0], fish[i][1]))
    
    
    if len(can_eat) == 0:
        break
    else:
        can_eat.sort(key=lambda x : (int(x[0]), int(x[1]), int(x[2])))
        fish.remove((can_eat[0][1], can_eat[0][2], graph[can_eat[0][1]][can_eat[0][2]]))
        result += can_eat[0][0]
        shark_eat += 1
        graph[can_eat[0][1]][can_eat[0][2]] = 0
        starty = can_eat[0][1]
        startx = can_eat[0][2]
        if (shark_eat == shark_size):
            shark_size += 1
            shark_eat = 0

print(result)
        