# https://school.programmers.co.kr/learn/courses/30/lessons/12904#
## 아쉬운점 : 문제 조건을 똑띠 읽어야한다..


def solution(s):
    answer = 0
    
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            right = s[i:j]
            if right == right[::-1]:
                answer = max(answer, len(right))
    
    
    
    return answer