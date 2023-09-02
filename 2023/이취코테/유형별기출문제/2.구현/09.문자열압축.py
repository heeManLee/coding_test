def solution(s):
    answer = 100000000
    temp = 0
    count = 1
    now = ""  
    if(len(s) == 1):
        answer = 1
    for i in range(1, len(s) // 2 + 1):
        temp = 0
        count = 1
        now = ""
        for j in range(len(s) // i):
            if(s[i*j:i*(j+1)] == s[i*(j+1):i*(j+2)]):
                now = s[i*j:i*(j+1)]
                count += 1
            else:
                if count == 1:
                    temp += i
                else:
                    temp += i + len(str(count))
                    count = 1
            if len(s[i*j:i*(j+1)]) != len(s[i*(j+1):i*(j+2)]):
                temp += len(s[i*(j+1):i*(j+2)])
     
        answer = min(answer, temp)
    
    

    return answer

solution("a")