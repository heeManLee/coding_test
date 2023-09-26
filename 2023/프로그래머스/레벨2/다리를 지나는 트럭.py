## 아쉬운점: 딕셔너리 왠만하면 쓰지 말자 좀.. 겹치는 숫자 있으면 ㅈ된다.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    wait = deque(truck_weights)
    now = deque()
    now_sum = 0
    while len(wait) > 0 or len(now) > 0:
        answer += 1
        to_delete = []
        for k in range(len(now)):
            now[k][1] += 1
            if now[k][1] == bridge_length + 1:
                now_sum -= now[k][0]
                to_delete.append(k)
        
        if to_delete:
            for i in to_delete:
                now.popleft()
        
        
        if wait and now_sum + wait[0] <= weight and len(now) < bridge_length:
            temp = wait.popleft()
            now_sum += temp
            now.append([temp, 1])    
    
    return answer