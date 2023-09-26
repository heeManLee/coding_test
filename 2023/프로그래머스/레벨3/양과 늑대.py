## 아쉬웠던 점 : 문제에서 입력 조건을 보고 코드를 생각해보자.. 충분히 풀 수 있엇던 문제였음

def solution(info, edges):
    
    visited = [0] * len(info)
    answer = []
        
    def go(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for p, s in edges:
            if visited[p] and not visited[s]:
                visited[s] = 1
                if info[s] == 0:
                    go(sheep+1, wolf)
                else:
                    go(sheep, wolf+1)
                visited[s] = 0
    
    visited[0] = 1
    go(1,0)
    
    return max(answer)