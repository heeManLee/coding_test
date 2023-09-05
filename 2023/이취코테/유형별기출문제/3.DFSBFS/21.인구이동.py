### 뭔가 한 사이클이 지나고 바뀐 맵을 만들 때는 그 결과를 만드는 과정에서 맵을 바꾸는 방법을 생각해보자

from collections import deque
import copy
n, l, r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

team_map = [[-1] * n for _ in range(n)]
temp_team_map = []
result = 0
count = 1



dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def find_count():
    global n, l, r, temp_team_map
    temp_count = 0
    
    temp_team_map = copy.deepcopy(team_map)
    temp_flag = 0
    for i in range(n):
        for j in range(n):
            if temp_team_map[i][j] == -1:
                q = deque()
                team_list = []
                temp_team_map[i][j] = temp_count
                q.append((i,j))
                team_list.append((i,j))
                team_num = 1
                team_sum = graph[i][j]
                while q:
                    y, x = q.popleft()
                    for dir in range(4):
                        ny = y + dy[dir]
                        nx = x + dx[dir]

                        if ny >= 0 and ny < n and nx >= 0 and nx < n:
                            if l <= abs(graph[y][x] - graph[ny][nx]) and abs(graph[y][x] - graph[ny][nx]) <= r and temp_team_map[ny][nx] == -1:
                                temp_team_map[ny][nx] = temp_count
                                q.append((ny,nx))
                                team_num += 1
                                team_sum += graph[ny][nx]
                                team_list.append((ny,nx))
                                temp_flag = 1
                
                for k in range(len(team_list)):
                    graph[team_list[k][0]][team_list[k][1]] = int(team_sum / team_num)

                temp_count += 1

    if(temp_flag == 1):
        return temp_count
    else:
        return 0


while count != 0:
    count = find_count()
    if count == 0:
        break
    else:
        result += 1



print (result)
