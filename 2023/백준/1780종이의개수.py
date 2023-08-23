n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

result = [0] * 3

## 0 ~ 8,  0~2 3~5 6~8, 0 1 2 3 4 5

def find(y, x, n):
    temp = graph[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if temp != graph[i][j]:
                for k in range(3):
                    for l in range(3):
                        find(y + k * (n//3), x + l * (n//3), n // 3)
                return

    if(temp == -1):
        result[0] += 1
    elif(temp == 0):
        result[1] += 1
    elif(temp == 1):
        result[2] += 1

find(0, 0, n)

for i in range(3):
    print(result[i])