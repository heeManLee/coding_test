import sys
input = sys.stdin.readline

## 1행부터 h행, 1열부터 n-1열까지
n, m, h = map(int, input().split())

connect = [[False] * (n+1) for _ in range(h+1)]

for i in range(m):
    a,b = map(int, input().split())
    connect[a][b] = True

def check():
    for j in range(1, n):
        start = j
        for i in range(1, h+1):
            if connect[i][start]:
                start = start + 1
            elif connect[i][start-1]:
                start = start - 1

        if start != j :
            return False
    
    return True

def setting(count, y, x):

    global answer
    if answer <= count:
        return

    if check():
        answer = min(answer, count)
        return
    
    if count == 3:
        return
    
    for i in range(y, h+1):

        if y == i:
            k = x
        else:
            k = 0

        for j in range(k, n):
            if connect[i][j] == True or connect[i][j+1] == True or connect[i][j-1] == True:
                continue
            else:
                connect[i][j] = True
                setting(count+1, i, j+2)
                connect[i][j] = False

answer = 4
setting(0, 1, 1)

if answer == 4:
    print(-1)
else:
    print(answer)