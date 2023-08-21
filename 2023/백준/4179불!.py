from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

canmove = deque()
fire = deque()



for j in range(n):
    for i in range(m):
        if graph[j][i] == 'J':
            canmove.append((j,i,0))
        if graph[j][i] == 'F':
            fire.append((j,i, 0))

flag = 0
now = 0
result = 100000000
while(canmove):
    while(fire and now == fire[0][2]):
        fy, fx, fcount = fire.popleft()
        for i in range(4):
            fny = fy + dy[i]
            fnx = fx + dx[i]

            if fny < 0 or fny >= n or fnx < 0 or fnx >= m or graph[fny][fnx] == '#' or graph[fny][fnx] == 'F':
                continue
            fire.append((fny,fnx, fcount+1))
            graph[fny][fnx] = 'F'
    

    while(canmove and now == canmove[0][2]):
        y, x, count = canmove.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                result = min(result, count+1)
                continue
            
            if graph[ny][nx] == '#' or graph[ny][nx] == 'F' or graph[ny][nx] == 'J':
                continue

            graph[ny][nx] = 'J'
            canmove.append((ny, nx, count+1))

    now += 1

if(result == 100000000):
    print("IMPOSSIBLE")
else:
    print(result)


