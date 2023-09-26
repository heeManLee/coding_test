## https://school.programmers.co.kr/learn/courses/30/lessons/42883?language=python3
## 아쉬운점 : 전체 경우가 어떻게 돌아가는지 구체화하는게 좀 어려운거 같다..

def solution(number, k):
    answer = []
    
    for i in number:
        if len(answer) == 0:
            answer.append(i)
            continue
        
        if k > 0:
            while answer[-1] < i:
                answer.pop()
                k -= 1
                if len(answer) == 0 or k <= 0:
                    break
        answer.append(i)
    
    if k > 0:
        answer = answer[:-k]
    
    return ''.join(answer)