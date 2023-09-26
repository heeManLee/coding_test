## https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3

answer = 0


def go(numbers, idx, result, target):
    global answer
    
    if idx == 5:
        if result == target:
            answer += 1
        return
    
    go(numbers, idx+1, result+numbers[idx], target)
    go(numbers, idx+1, result-numbers[idx], target)
    


def solution(numbers, target):
    
    go(numbers, 0, 0, target)
    
    return answer

solution([4, 1, 2, 1], 4)