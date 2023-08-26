def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    answer = 0
    
    parent = [0] * (n+1)
    
    for i in range(1, n+1):
        parent[i] = i
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if computers[i-1][j-1] == 1:
                union_parent(parent, i, j)
    
    result = set()
    for i in range(1, len(parent)+1):
        result.add(parent[i])
        
solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])