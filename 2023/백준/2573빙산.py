from collections import deque

n, m = map(int, input().split())

array = []
ice = {}
for i in range(n):
    array.append(list(map(int, input().split())))

#################### 짱 중요했음
#### 찾아본거 2
for j in range(n):
    for i in range(m):
        if array[j][i] > 0:
            if j not in ice:
                ice[j] = {}
            ice[j][i] = array[j][i]


result = 10000000
year = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def checkice():
    global result, year
    ###### 찾아본거 1
    visited = [[False] * m for _ in range(n)]
    total = 0
    for j in range(n):
        for i in range(m):
            if(array[j][i] != 0 and visited[j][i] == False):
                visited[j][i] = True
                q = deque()
                q.append((j,i))
                while q:
                    temp = q.popleft()
                    for i in range(4):
                        ny = temp[0] + dy[i]
                        nx = temp[1] + dx[i]
                        if(ny < 0 or ny >= n or nx < 0 or nx >= m):
                            continue

                        if(array[ny][nx] != 0 and visited[ny][nx] == False):
                            visited[ny][nx] = True
                            q.append((ny, nx))
                total += 1
    if total >= 2:
        result = min(result, year)

def update():
    for j in ice:
        for i in ice[j]:
            array[j][i] = ice[j][i]
                

def oneyear():
    global year
    ###### 중요한거! 지워야 할 것은 중복이 될 수 있으니 set로 구현
    to_deleate = set()
    for j in ice:
        for i in ice[j]:
            for k in range(4):
                ny = j + dy[k]
                nx = i + dx[k]
                if(ny < 0 or ny >= n or nx < 0 or nx >= m):
                    continue                

                if array[ny][nx] == 0:
                    ice[j][i] -= 1
                    if ice[j][i] <= 0:
                        ##### set에 넣을 때는 add로 넣어야함
                        to_deleate.add((j, i))
                        ice[j][i] = 0
    update()
    year += 1
    for j, i in to_deleate:
        ###### 딕셔너리에 넣은 것은 del로 지울 수 있음
        del ice[j][i]
        if not ice[j]:
            del ice[j]

while(ice):
    checkice()
    oneyear()
    if result != 10000000:
        break

if result != 10000000:
    print(result)
else:
    print(0)

