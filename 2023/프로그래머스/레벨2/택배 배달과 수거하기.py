## https://school.programmers.co.kr/learn/courses/30/lessons/150369
## 최소거리를 나타낼 때 앞의 결과를 -가 되면 뒤에 영향을 준다고 생각하고 풀어도 된다.. 어렵게 생각하기 ㄴㄴ

def solution(cap, n, deliveries, pickups):
    answer = 0
    delive = 0
    pickup = 0
    
    for i in range(n):
        delive += deliveries[n-i-1]
        pickup += pickups[n-i-1]
        
        while delive > 0 or pickup > 0:
            delive -= cap
            pickup -= cap
            answer += 2* (n - i)
    
    return answer