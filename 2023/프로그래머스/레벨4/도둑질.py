## https://school.programmers.co.kr/learn/courses/30/lessons/42897
## 생각할만한점 : 원으로 되어 있는 DP는 경우를 나눠서도 생각할 수 있다.

def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(max(dp1), max(dp2))