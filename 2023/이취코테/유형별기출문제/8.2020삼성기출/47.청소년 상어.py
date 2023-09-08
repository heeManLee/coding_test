from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0 , -1]
dx = [0, -1, -1, -1, 0 , 1, 1, 1]

fisrt_graph = [[(0,0)] * 4 for _ in range(4)]
first_fish = []

## 그래프상 : 번호, 방향
for i in range(4):
    temp_array = list(map(int, input().split()))
    j = 0
    for k in range(4):
        first_fish.append([temp_array[j], temp_array[j+1] - 1, i, k])
        fisrt_graph[i][k] = [temp_array[j],temp_array[j+1] - 1]
        j+=2

## 물고기 : 번호, 방향, y, x 
## 상어 : y, x, 방향
first_shark = [0, 0, fisrt_graph[0][0][1]]
score = fisrt_graph[0][0][0]
result = 0
first_fish.remove([fisrt_graph[0][0][0], fisrt_graph[0][0][1], 0, 0])
fisrt_graph[0][0] = [0,0]
def fishmove(shark, temp_graph, temp_fish):
    for i in range (len(temp_fish)):
        size = temp_fish[i][0]
        d = temp_fish[i][1]
        y = temp_fish[i][2]
        x = temp_fish[i][3]
        turn = 0
        while(1):
            if turn == 8:
                break

            ny = y + dy[d]
            nx = x + dx[d]
            if (ny == shark[0] and nx == shark[1]) or ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                turn += 1
                d = (d + 1) % 8
                temp_fish[i][1] = d
                continue
            else:
                temp_graph[ny][nx], temp_graph[y][x] = temp_graph[y][x], temp_graph[ny][nx]
                temp_graph[ny][nx][1] = temp_fish[i][1]
                if temp_graph[y][x][0] != 0:
                    for k in range(len(temp_fish)):
                        if temp_fish[k][2] == ny and temp_fish[k][3] == nx:
                            change_fish = k
                            break

                    temp_fish[i][2], temp_fish[i][3], temp_fish[change_fish][2], temp_fish[change_fish][3] = temp_fish[change_fish][2], temp_fish[change_fish][3], temp_fish[i][2], temp_fish[i][3]                
                    break
                else:
                    temp_fish[i][2], temp_fish[i][3] = ny, nx
                    break
        
    return temp_graph, temp_fish

def sharkmove(shark, graph, flag):
    can_eat = []
    y = shark[0]
    x = shark[1]
    d = shark[2]
    while(1):
        y = y + dy[d]
        x = x + dx[d]
        if y < 0 or y >= 4 or x < 0 or x >= 4:
            break

        if graph[y][x][0] == 0:
            continue

        can_eat.append((y,x))
    if len(can_eat) == 0:
        flag = 0
        return False, flag
    else:
        return can_eat, flag

    



def go(shark, graph, fish, flag, score):
    global result
    fish.sort()
    if (flag == 0):
        result = max(score, result)
        return
    graph, fish = fishmove(shark, graph, fish)
    can_eat, flag = sharkmove(shark, graph, flag)
    if can_eat:
        for i in range(len(can_eat)):
            ## 물고기 : 번호, 방향, y, x 
            ## 상어 : y, x, 방향
            before_size = graph[can_eat[i][0]][can_eat[i][1]][0]
            before_dir = graph[can_eat[i][0]][can_eat[i][1]][1]
            before_y = can_eat[i][0]
            before_x = can_eat[i][1]
            shark = [before_y, before_x, before_dir]


            fish.remove([before_size, before_dir, before_y, before_x])
            score += before_size
            graph[before_y][before_x] = [0,0]
            go(shark, deepcopy(graph), deepcopy(fish), flag, score)
            fish.append([before_size, before_dir, before_y, before_x])
            graph[before_y][before_x] = [before_size, before_dir]
            score -= before_size
    else:
        result = max(score, result)
        return

go(first_shark, fisrt_graph, first_fish, 1, score)


print(result)