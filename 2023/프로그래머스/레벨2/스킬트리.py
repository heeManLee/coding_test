## https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    
    goal_len = len(skill)
    
    for i in range(len(skill_trees)):
        flag = 1
        count = 0
        for k in range(len(skill_trees[i])):
            if skill_trees[i][k] in skill:
                if skill_trees[i][k] == skill[count]:
                    count += 1
                    if count == goal_len:
                        break
                else:
                    flag = 0
                    break
        if flag:
            answer += 1
    
    return answer