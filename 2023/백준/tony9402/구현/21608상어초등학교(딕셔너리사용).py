## 딕셔너리 사용해서 in 을 사용한 문제이다.. 그동안 햇갈렸던게 있어서 중요하다.
## 최대값을 시작할 때는 -1로 시작해야한다.
import sys

input = sys.stdin.readline

n = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
graph = [[0] * (1+n) for _ in range(1+n)]

total = {}
for s in range(n*n):
    t, a, b, c, d = map(int, input().split())
    friend = [a, b, c, d]
    total[t] = friend
    mnearf = -1
    mnear0 = -1
    y = 1
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            nearf = 0
            near0 = 0
            if graph[i][j] != 0:
                continue

            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if ny <= 0 or ny > n or nx <= 0 or nx > n:
                    continue
                if graph[ny][nx] in friend:
                    nearf += 1
                if graph[ny][nx] == 0:
                    near0 += 1
            
            if mnearf > nearf:
                continue
            else:
                if mnearf == nearf:
                    if mnear0 >= near0:
                        continue
                    else:
                        mnear0 = near0
                        y = i
                        x = j
                elif mnearf < nearf:
                    mnearf = nearf
                    mnear0 = near0
                    y = i
                    x = j
    graph[y][x] = t

result = 0
for i in range(1, 1+n):
    for j in range(1, 1+n):
        count = 0
        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if ny <= 0 or ny > n or nx <= 0 or nx > n:
                continue

            if graph[ny][nx] in total[graph[i][j]]:
                count += 1
        if count == 0:
            continue
        else:
            result += 10 ** (count-1)

print(result)
            