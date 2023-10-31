## https://school.programmers.co.kr/learn/courses/30/lessons/150367#
## 자식노드가 탐색순으로 했을때 부모의 양 옆 노드에 붙어있는게 아니다.
## 이진수 만드는 건 잘 했는데, 자식 노드를 탐색하는 과정이 많이 약하다.


def search(number):
    length = len(number)
    if length == 1 or 1 not in number or 0 not in number:
        return True
    
    mid = length // 2
    if number[mid] == 0:
        return False
    
    return search(number[:mid]) and search(number[mid+1:])

def solution(numbers):
    answer = []

    for num in numbers:
        temp = []
        temp_num = num
        while temp_num >= 1:
            temp.append(temp_num % 2)
            temp_num = temp_num // 2

        temp_len = len(temp)
        count = 0
        while temp_len > 0:
            count += 1
            temp_len = temp_len // 2

        for i in range(len(temp), 2 ** count - 1):
            temp.append(0)

        temp = temp[::-1]
        
        answer.append(1 if search(temp) else 0)

    return answer