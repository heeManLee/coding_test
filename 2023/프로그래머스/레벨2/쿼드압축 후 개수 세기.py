## https://school.programmers.co.kr/learn/courses/30/lessons/68936?language=python3
## 사각형 계속 /2 하면서 쪼개는 좋은 예제

def solution(arr):
    answer = [0, 0]
    length = len(arr)
    def find(a, b, l):
        start = arr[a][b]
        for i in range(a, a+l):
            for j in range(b, b+l):
                if arr[i][j] != start:
                    l = l // 2
                    find(a, b, l)
                    find(a, b+l, l)
                    find(a+l, b, l)
                    find(a+l, b+l, l)
                    return
        answer[start] += 1
    
    find(0, 0, length)
    return answer