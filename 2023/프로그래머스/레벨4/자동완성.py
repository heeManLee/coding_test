## https://school.programmers.co.kr/learn/courses/30/lessons/17685
### 이걸 어케품??
def solution(words):
    answer = 0
    Trie = {}
    
    for word in words:
        cur_Trie = Trie
        for x in word:
            cur_Trie.setdefault(x, [0,{}])
            cur_Trie[x][0] += 1
            cur_Trie = cur_Trie[x][1]

    
    for word in words:
        cur_Trie = Trie
        for i in range(len(word)):
            if cur_Trie[word[i]][0] == 1:
                break
            cur_Trie = cur_Trie[word[i]][1]
        answer += (i+1)
    return answer

solution(["go","gone","guild"])