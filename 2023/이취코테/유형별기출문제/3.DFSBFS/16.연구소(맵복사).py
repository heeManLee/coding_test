n, m = map(int, input().split())
temp = [[0] * m for _ in range(n)]

graph = []
result = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def check(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny >= 0 and ny < n and nx >= 0 and nx < m:
            if temp[ny][nx] == 0:
                temp[ny][nx] = 2
                check(ny, nx)


def score():
    sco = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                sco += 1
    
    return sco


def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    check(i, j)
        result = max(result, score())
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1


dfs(0)

print(result)
