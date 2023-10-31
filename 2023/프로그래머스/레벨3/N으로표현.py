### https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op2 - op1)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
                    
                    if op1 != 0:
                        dp[i].add(op2 // op1)
        if number in dp[i]:
            return i
    return -1