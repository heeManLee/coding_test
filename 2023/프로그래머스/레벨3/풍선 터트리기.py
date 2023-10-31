##https://school.programmers.co.kr/learn/courses/30/lessons/68646
## 아쉬운점 : 실제로 나왔으면 아마.. 틀렸을 가능성이 클 거 같다.. 온몸 비틀기를 해도 힘들었을듯..
##           이런 문제가 나오면 일단 빈 종이에 예제들을 적고 이것들이 왜 이렇게 되는지 생각을 해봐야 할 듯 하다.

def solution(a):
    answer = 0
    left_min = [1000000001] * len(a)
    right_min = [1000000001] * len(a)
    left_min[0] = a[0]
    right_min[-1] = a[-1]
    
    for i in range(1, len(a)):
        left_min[i] = min(left_min[i-1], a[i])
    
    for i in range(len(a)-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i])
    
    for i in range(len(a)):
        if left_min[i] < a[i] and right_min[i] < a[i]:
            answer += 1
    
    
    return len(a) - answer