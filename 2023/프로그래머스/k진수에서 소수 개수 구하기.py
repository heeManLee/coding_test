import math
from collections import deque

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    


def solution(n, k):
    answer = 0
    
    temp = []
    while(n != 0):
        temp.append(n % k)
        n = n // k
        
    temp.reverse()
    
    result = []
    temp_str = ""
    for i in range(len(temp)):
        if temp[i] == 0 and temp_str != "":
            result.append(int(temp_str))
            temp_str = ""
        elif temp[i] != 0:
            temp_str += str(temp[i])
    
    if(temp_str != ""):
        result.append(int(temp_str))

    for i in result:
        if(is_prime_number(i)):
            answer += 1
    
    return answer

print(solution(10000, 10))