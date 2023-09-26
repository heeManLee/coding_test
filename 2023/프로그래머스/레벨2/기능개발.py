## 아쉬운 점 : 시뮬레이션 문제에서 본체를 건드리는 코드는 위험하다. visit를 활용하자
            ## deque을 쓰는 거에 함몰되어 있는 것 같다. 배열로 바로 쓸 수 있으면 그렇게 하자.

from collections import deque

def solution(progresses, speeds):
    answer = []
    
    pro = deque(progresses)
    visit = [0] * len(progresses)
    idx = 0
    while (idx < len(speeds)):
        for i in range(len(speeds)):
            if visit[i] == 0:
                pro[i] += speeds[i]
        
        if pro[idx] >= 100:
            count = 0
            for i in range(idx, len(pro)):
                if pro[i] >= 100 and visit[i] == 0:
                    visit[i] = 1
                    count += 1
                    idx += 1
                else:
                    break
            answer.append(count)
                
    return answer

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])