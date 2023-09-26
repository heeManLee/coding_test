## 아쉬운점 : 1. 여러 괄호 나오는 거는 무조건 스택 느낌으로 풀어야 한다.
##           2. 리스트 append 뿐 만 아니라 pop도 있다. -> 스택 바로 사용 가능
from collections import deque

def check(x):
    
    temp = []
    for i in x:
        if len(temp) == 0:
            temp.append(i)
        else:
            if i == ")" and temp[-1] == "(":
                temp.pop()
            elif i == "]" and temp[-1] == "[":
                temp.pop()
            elif i == "}" and temp[-1] == "{":
                temp.pop()
            else:
                temp.append(i)
    if len(temp) == 0:
        return True
    else:
        return False
    

def solution(s):
    answer = 0
    s = deque(s)
    s_len = len(s)
    for i in range(s_len):
        if check(s):
            answer += 1
        s.append(s.popleft())
    
    return answer