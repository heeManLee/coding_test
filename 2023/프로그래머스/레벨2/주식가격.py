## 아쉬운 점 : 그냥 문제에서 나온 순서대로 구현을 하면 된다. 어렵게 생각하지 말자.
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] <= prices[j]:
               continue
            else:
                break
        answer.append(count)
         
    return answer

solution([1, 2, 3, 2, 3])