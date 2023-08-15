def dfs(graph, num, visited):
    visited[num] = True
    print(num, end=' ')
    for i in graph[num]:
        if visited[i] == False:
            dfs(graph, i, visited)


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visit = [False] * 9

dfs(graph, 1, visit)