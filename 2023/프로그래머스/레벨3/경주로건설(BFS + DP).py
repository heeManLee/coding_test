## https://school.programmers.co.kr/learn/courses/30/lessons/67259

## BFS + DP
## 무조건 popleft를 해야한다.. 억까당하기 싫으면..

from collections import deque
from copy import deepcopy
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def solution(board):
    answer = int(1e9)
    n = len(board)
    m = len(board[0])
    
    for i in range(2):
        d = i*2
        visit = [[100000000] * m for _ in range(n)]
        history = 0
        q = deque()
        visit[0][0] = 0
        q.append([(0,0), d, 0]) ## y,x  방향,  cost
        
        while q:
            now, n_dir, n_cost = q.popleft()
            
            y = now[0]
            x = now[1]   
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m or board[ny][nx] == 1:
                    continue

                if n_dir == i:
                    cost = n_cost + 100
                else:
                    cost = n_cost + 600
                
                if cost < visit[ny][nx]:
                    visit[ny][nx] = cost
                    q.append([[ny,nx], i, cost])
        
        answer = min(answer, visit[-1][-1])
    
                
    return answer


solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])