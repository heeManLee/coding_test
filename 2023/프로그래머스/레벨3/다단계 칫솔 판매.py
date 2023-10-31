## https://school.programmers.co.kr/learn/courses/30/lessons/77486
## 딕셔너리를 쓰면 세상이 편해진다.

def solution(enroll, referral, seller, amount):
    answer = []
    
    result = {}
    for i in enroll:
        result[i] = 0
        
    refer = {}
    for i in range(len(referral)):
        refer[enroll[i]] = referral[i]
        
    for i in range(len(seller)):
        money = amount[i] * 100
        now = seller[i]
        while money > 0:
            reward = int(money * (0.1))
            if reward == 0:
                result[now] += money
                break
            elif refer[now] == '-':
                result[now] += (money - reward)
                break
            result[now] += (money - reward)
            money = reward
            now = refer[now]
    
    answer = list(result.values())
    return answer