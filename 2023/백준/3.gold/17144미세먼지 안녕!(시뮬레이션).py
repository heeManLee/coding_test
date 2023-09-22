## 시뮬레이션 문제
## 시뮬레이션 끝나고 더해주는거는 tmp_arr를 만들어서 만들고 더해주자
## 위치 바꾸는 거는 graph[y][x], before = before, graph[y][x] 를 해서 before에 다음 값이 저장되게 하면 좋다.
## 일직선으로 가는거는 while True: 를 꼭 하는게 좋다
## dy dx를 꼭 전역으로 할 필요는 없다.. 함수 안에서 새로 지정해주는게 더 편할듯
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

graph = []
for i in range(r):
    graph.append(list(map(int, input().split())))

up = -1
down = -1
for i in range(r):
    if graph[i][0] == -1:
        up = i
        down = i+1
        break


def spread():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    tmp_arr = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                tmp = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != -1:
                        tmp_arr[ny][nx] += graph[i][j] // 5
                        tmp += graph[i][j] // 5
                
                graph[i][j] -= tmp
    for i in range(r):
        for j in range(c):
            graph[i][j] += tmp_arr[i][j]
    
def wind_up():
    global up
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    direct = 0
    before = 0
    y, x = up, 1
    while True:
        ny = y + dy[direct]
        nx = x + dx[direct]
        if y == up and x == 0:
            break
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            direct += 1
            continue

        graph[y][x], before = before, graph[y][x]

        y = ny
        x = nx

def wind_down():
    global down
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    direct = 0
    before = 0
    y, x = down, 1
    while True:
        ny = y + dy[direct]
        nx = x + dx[direct]
        if y == down and x == 0:
            break
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            direct += 1
            continue

        graph[y][x], before = before, graph[y][x]

        y = ny
        x = nx
while(t>0):
    t -= 1
    spread()
    wind_up()
    wind_down()
    
result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] != 0 and graph[i][j] != -1:
            result += graph[i][j]

print(result)