##https://school.programmers.co.kr/learn/courses/30/lessons/42627
## heapq 써서 푸는 건데 이거 어케품??

import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    q = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(q, [j[1], j[0]])
        
        if len(q) > 0 :
            cur = heapq.heappop(q)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1
    
    
    return answer // len(jobs)