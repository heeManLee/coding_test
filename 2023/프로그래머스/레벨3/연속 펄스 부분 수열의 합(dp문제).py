## 뻔한 dp문제.. 전에 값이 음수이면 0으로 컷해주는 방법을 알았으면 풀 수 있었을듯??

def solution(sequence):
    answer = -10000000
    
    dp = [[0, 0] for _ in range(len(sequence))]
    
    dp[0][0], dp[0][1] = sequence[0] * -1, sequence[0]
    
    answer = max(answer, max(dp[0]))
    
    for idx, val in enumerate(sequence):
        if idx == 0:
            continue
        
        if idx % 2 == 0:
            dp[idx][0] = max(dp[idx-1][0], 0) + val * -1
            dp[idx][1] = max(dp[idx-1][1], 0) + val     
        else:
            dp[idx][0] = max(dp[idx-1][0], 0) + val 
            dp[idx][1] = max(dp[idx-1][1], 0) + val * -1
        
        answer = max(answer, max(dp[idx]))
    
    return answer