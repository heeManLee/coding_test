# https://school.programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    answer = 0
    works.sort(reverse = True)
    while n > 0:
        max_num = works[0]
        if max_num == 0:
            break

        start = 0
        while start < len(works) and works[start] == max_num and n > 0 :
            if works[start] == 0:
                break
            works[start] -= 1
            n -= 1
            start += 1
            
    for i in works:
        if i != 0:
            answer += i ** 2
        
    return answer

solution(99, [2, 15, 22, 55, 55])