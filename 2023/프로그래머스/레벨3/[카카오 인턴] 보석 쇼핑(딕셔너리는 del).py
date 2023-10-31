## 잘 했던 점 : 1. l, r을 나누고 생각했던 점
## 아쉬웠던 점 : 1. l과 r은 반드시 0에서 부터 시작하는 것으로 하자, 2. 개수 세는 거는 deque보다 반드시 dict를 사용 하는게 좋다.
##              3. dict에서 del 쓰는거를 반드시 생각을 해야 할듯 하다., 4. answer 초기값을 잘 설정해서 모든 과정 결과를 저장할 필요가 없도록 해야한다.
##              5. len(dict)는 개수를 알려준다, 6. len(set(gems)) 처럼 리스트를 set 형태로 바꿔서 생각할 수 있어야 한다.

def solution(gems):
    answer = [0, len(gems)] 
    goal_len = len(set(gems))
    process = {}

    l = 0
    r = 0
    while (r < len(gems)):
        if gems[r] not in process:
            process[gems[r]] = 1
        else:
            process[gems[r]] += 1

        while(len(process) == goal_len):
            if r - l < answer[1] - answer[0]:
                answer = [l, r]
            
            process[gems[l]] -= 1
            if process[gems[l]] == 0:
                del process[gems[l]]  ## 매우 중요하다
            l += 1
            
        
        r += 1
    return [answer[0] + 1, answer[1] + 1]


solution(["AA", "AB", "AC", "AA", "AC"])