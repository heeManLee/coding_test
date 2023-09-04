import copy
from collections import deque
n = int(input())

graph = []
teacher = []

for i in range(n):
    graph.append(input().split())

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

flag = 0

def find():
    for i in range(len(teacher)):
        y = teacher[i][0]
        x = teacher[i][1]
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            while ny >= 0 and ny < n and nx >= 0 and nx < n:
                if graph[ny][nx] == 'S':
                    return False
                elif graph[ny][nx] == 'O' or graph[ny][nx] == 'T':
                    break
                ny += dy[dir]
                nx += dx[dir]
    return True


def go(count):
    global flag
    if count == 3:
        if (find()):
            flag = 1
            return
        else:
            return
    
    
    for i in range(n):
        for j in range(n):
            if flag == 0:
                if graph[i][j] == 'X':
                    count += 1
                    graph[i][j] = 'O'
                    go(count)
                    count -= 1
                    graph[i][j] = 'X'

go(0)

if(flag):
    print("YES")
else:
    print("NO")