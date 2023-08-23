import sys
from collections import deque

input = sys.stdin.readline

array = []

n = int(input())
for i in range(n):
    array.append(list(map(int, input().split())))

dy = [1, 0]
dx = [0, 1]

visited = [[False] * n for _ in range(n)]
q = deque()
visited[0][0] = True
q.append((0,0))

goal = 0
while q and goal == 0:
    temp = q.popleft()
    for i in range(2):
        #### 간단한건데 배열을 잘 못 써서 시간 걸림
        ny = temp[0] + dy[i] * array[temp[0]][temp[1]]
        nx = temp[1] + dx[i] * array[temp[0]][temp[1]]
        if(ny < 0 or ny >= n or nx < 0 or nx >= n):
            continue

        if(array[ny][nx] == -1):
            goal = 1
            break
        if(visited[ny][nx] == False):
            visited[ny][nx]= True
            q.append((ny,nx))


if(goal == 1):
    print("HaruHaru")
else:
    print("Hing")