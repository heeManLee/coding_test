import math

n, m = map(int, input().split())
result = 10000000
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * (n) for _ in range(n)]
chick = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))



def find_distance():
    global chick
    global house
    distance = 0
    for i in range(len(house)):
        temp = 10000000
        for j in range(len(chick)):
            temp = min(temp, abs(house[i][0] - chick[j][0]) + abs(house[i][1] - chick[j][1]))
        distance += temp
    return distance


def find_chick(ny, nx):
    global chick
    global result
    if(len(chick) == m):
        result = min(result, find_distance())
        return
    
    for i in range(ny, n):
        for j in range(0, n):
            if graph[i][j] == 2 and visited[i][j] == 0:
                visited[i][j] = 1
                chick.append([i, j])
                find_chick(i,j)
                visited[i][j] = 0
                chick.remove([i,j])

find_chick(0, 0)
print(result)
