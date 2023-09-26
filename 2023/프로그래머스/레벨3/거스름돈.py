# https://school.programmers.co.kr/learn/courses/30/lessons/12907?language=python3
# 이걸 어케 푸는 것일까.. DP는 참 어렵다..

def solution(n, money):
    dp = [1] + [0] * n
    
    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                dp[price] += dp[price - coin]
    
    return dp[n] % 1000000007