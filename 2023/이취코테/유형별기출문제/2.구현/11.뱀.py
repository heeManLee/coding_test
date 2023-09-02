from collections import deque

n = int(input())
apple_count = int(input())

graph = [[0] * (n) for _ in range(n)]

for i in range(apple_count):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 'A'

move_count = int(input())

move_list = deque()
for i in range(move_count):
    a, b = input().split()
    move_list.append((int(a),b))
graph[0][0] = 1

body = deque()
body.append((0,0))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
# 오른쪽0 -> (-1, 1) -> (3, 1) -1 +1
# 아래1 -> (1, -1) -> (0, 2)  -1 +1
# 왼쪽2 -> (1, -1) -> (1, 3)  -1 +1
# 위3 -> (-1, 1) -> (2, 0)   -1 +1
flag = 1
dir = 0
head = (0, 0)

def move(dir, graph):
    global flag
    global head
    ny = head[0] + dy[dir]
    nx = head[1] + dx[dir]
    head = (ny, nx)
    if(ny < 0 or ny >= n or nx < 0 or nx >= n or graph[ny][nx] == 1):
        flag = 0
        return graph
    
    body.append((ny, nx))
    if(graph[ny][nx] == 'A'):
        graph[ny][nx] = 1   
    else:
        graph[ny][nx] = 1
        tail = body.popleft()
        graph[tail[0]][tail[1]] = 0
    return graph

def turn(a):
    global dir
    if a == 'L':
        if dir == 0:
            dir = 3
        else:
            dir -= 1
    elif a == 'D':
        if dir == 3:
            dir = 0
        else:
            dir += 1

time = 0
move_first = move_list.popleft()
while(flag):
    if(time == move_first[0]):
        turn(move_first[1])
        if(move_list):
            move_first = move_list.popleft()
    move(dir, graph)
    time += 1

print(time)