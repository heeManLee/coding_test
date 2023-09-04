## 리스트를 덱으로 바꾸는거 + 시간을 값으로 생각하는거
from collections import deque
n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

gt, gy, gx = map(int, input().split())

time = 0
gy -= 1
gx -= 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    virus, s, y, x = q.popleft()
    if s == gt:
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= 0 and ny < n and nx >=0 and nx < n:
            if graph[ny][nx] == 0:
                graph[ny][nx] = virus
                q.append((virus, s+1, ny, nx))

print(graph[gy][gx])