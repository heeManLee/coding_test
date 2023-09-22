import sys

n = input()
m = input()

graph = [[0] * (len(m) + 1) for _ in range(len(n)+1)]


for i in range(0, len(n)):
    for j in range(0, len(m)):
        if n[i] == m[j]:
            graph[i+1][j+1] = graph[i][j] + 1
        else:
            graph[i+1][j+1] = max(graph[i][j+1], graph[i+1][j])

print(graph[len(n)][len(m)])