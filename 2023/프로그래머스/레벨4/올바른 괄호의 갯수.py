answer = 0

def go(count, n, goal):
    global answer
    if n == goal and count == 0:
        answer += 1
        return
    
    if count < 0 or count + n > goal:
        return
    
    go(count+1, n, goal)
    go(count-1, n+1, goal)
    

def solution(n):
    global answer
    go(1, 0, n)
    
    return answer

solution(2)