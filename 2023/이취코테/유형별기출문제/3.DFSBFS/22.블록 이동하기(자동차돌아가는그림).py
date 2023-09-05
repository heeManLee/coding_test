## 바퀴 양쪽을 left, right가 아니라 set로 관리하는 방법

from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_y, pos1_x, pos2_y, pos2_x = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    ## 그냥 움직일 때
    for i in range(4):
        pos1_next_y, pos1_next_x, pos2_next_y, pos2_next_x = pos1_y + dy[i], pos1_x + dx[i], pos2_y + dy[i], pos2_x + dx[i]
        if board[pos1_next_y][pos1_next_x] == 0 and board[pos2_next_y][pos2_next_x] == 0:
            next_pos.append({(pos1_next_y, pos1_next_x), (pos2_next_y, pos2_next_x)})
    ## 가로로 있을 때
    if pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_y + i][pos1_x] == 0 and board[pos2_y + i][pos2_x] == 0:
                next_pos.append({(pos2_y + i, pos2_x), (pos2_y, pos2_x)})
                next_pos.append({(pos1_y + i, pos1_x), (pos1_y, pos1_x)})
    ## 새로로 있을 때
    elif pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_y][pos1_x + i] == 0 and board[pos2_y][pos2_x + i] == 0:
                next_pos.append({(pos2_y, pos2_x + i), (pos2_y, pos2_x)})
                next_pos.append({(pos1_y, pos1_x + i), (pos1_y, pos1_x)})
    return next_pos            
    


def solution(board):
    
    ## 외각을 1로 두르면 범위 판정을 더 쉽게 할 수 있다.
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    q = deque()
    visited = []
    pos = {(1,1), (1,2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n,n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    
    
    
    return 0

print(solution(	[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))