## https://school.programmers.co.kr/learn/courses/30/lessons/64064?language=python3
## 아쉬운 점 : 중복되는 리스트를 set에 추가할 때는 tuple의 형태로 넣어주어야 한다.

answer = set()

def go(user_id, banned_id, idx, count, visited):
    if count == len(banned_id):
        answer.add(tuple(visited))
        # print(visited)
        # print(answer)
        return
    
    for i in range(idx, len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]) and visited[j] == 0:
                flag = 1
                for k in range(len(banned_id[i])):
                    if banned_id[i][k] == '*':
                        continue
                    
                    if banned_id[i][k] != user_id[j][k]:
                        flag = 0
                        break
                        
                if flag and visited[j] == 0:
                    visited[j] = 1
                    
                    go(user_id, banned_id, i+1, count+1, visited)
                    visited[j] = 0
                    

def solution(user_id, banned_id):
    
    visited = [0] * len(user_id)
    go(user_id, banned_id, 0, 0, visited)
    print(answer)
    
    return len(answer)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])