import copy
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

dy = [-1, 0, 1]
dx = [1, 1, 1]
for t in range(T):
    result = 0
    array = []
    n, m = map(int, input().split())
    temp_array = list(map(int, input().split()))
    for i in range(n):
        array.append(temp_array[m*i : m*(i+1)])
    
    for i in range(n):
        dupli = copy.deepcopy(array)
        temp_max = 0
        q = deque()
        start = (i, 0)
        q.append(start)
        while q:
            now = q.popleft()
            for d in range(3):
                ny = now[0] + dy[d]
                nx = now[1] + dx[d]

                if 0 <= ny and ny < n and 0 <= nx and nx < m:
                    if dupli[ny][nx] < array[ny][nx] + dupli[now[0]][now[1]]:
                        dupli[ny][nx] = array[ny][nx] + dupli[now[0]][now[1]]
                        q.append((ny, nx))
                        if nx == m-1:
                            temp_max = max(temp_max, dupli[ny][nx])
        result = max(result, temp_max)
    print(result)
    
                

