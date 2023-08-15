n, m = map(int, input().split())

y, x, state = map(int, input().split())


d = [[0] * m for _ in range(n)]
d[y][x] = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

result = 1
while(1):
    count = 0
    while(count < 4):
        ny = y + dy[(state+3)%4]
        nx = x + dx[(state+3)%4]
        if  ny<0 or ny>=n or nx<0 or nx>=m:
            count += 1
            state = (state+3)%4
            continue

        if array[ny][nx] == 1 or d[ny][nx] == 1:
            count += 1
            state = (state+3)%4
            continue

        state = (state+3)%4
        d[ny][nx] = 1
        y = ny
        x = nx
        count = 0
        result += 1

    ny = y + dy[(state+2)%4]
    nx = x + dx[(state+2)%4]
    if(ny<0 or ny>=n or nx<0 or nx>=m or array[ny][nx] == 1):
        break
    y = ny
    x = nx

print(result)

    
    

