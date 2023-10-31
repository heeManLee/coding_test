## https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = 1000000000
    
    for i in range(1, len(s) // 2 + 1):
        temp = 0
        count = 1
        for j in range(len(s) // i):
            print(s[i*j:i*(j+1)])
            if s[i*j:i*(j+1)] == s[i*(j+1) : i*(j+2)]:
                count += 1
            else:
                if count == 1:
                    temp += len(s[i*j:i*(j+1)])
                else:
                    temp += i + len(str(count))
                    count = 1
            
            if len(s[i*j:i*(j+1)]) != len(s[i*(j+1) : i*(j+2)]):
                temp += len(s[i*(j+1) : i*(j+2)])
        
        answer = min(answer, temp)
            
    return answer

solution("aabbaccc")