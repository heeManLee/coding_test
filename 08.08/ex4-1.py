n = int(input())
y, x = 1, 1
plans = input().split()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
move_types = ['U', 'D', 'L', 'R']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            ny = y+dy[i]
            nx = x+dx[i]
    
    if ny<1 or ny>n or nx<1 or nx>n:
        continue

    y, x =ny, nx

print(y, x)