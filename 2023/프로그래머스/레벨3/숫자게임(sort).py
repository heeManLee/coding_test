# https://school.programmers.co.kr/learn/courses/30/lessons/12987
## 배열에 del을 쓸 수가 있었다..? 지리네

def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    
    for a in A:
        if a >= B[0]:
            continue
        else:
            answer += 1
            del B[0]
    
    return answer