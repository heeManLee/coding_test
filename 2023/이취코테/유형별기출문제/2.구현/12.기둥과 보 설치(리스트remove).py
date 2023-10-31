## build_fram 위치, 위치, (기둥,보), (삭제, 설치)
## answer 규칙 위치, 위치, (기둥, 보)
## 기둥 설치 : 2, 보 설치 : 1로 graph에 값 넣기


## https://school.programmers.co.kr/learn/courses/30/lessons/60061
def possible(answer):
    for x, y, obj in answer:
        ## 기둥
        if obj == 0:
            if y==0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        ## 보
        else:
            if [x, y-1 ,0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    
    return True

def solution(n, build_frame):
    answer = []
    
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for build in build_frame:
        x, y, obj, craft = build
        #설치
        if craft == 1:
            answer.append([x,y,obj])
            if not possible(answer):
                answer.remove([x, y, obj])
        #삭제
        else:
            answer.remove([x,y,obj])
            if not possible(answer):
                answer.append([x,y,obj])
    return sorted(answer)