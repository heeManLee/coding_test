n = int(input())
start = 0
back = 0


graph = [0] * 366

for i in range(n):
    n, m = map(int, input().split())
    if i == 0:
        start = n
    for i in range(n, m+1):
        graph[i] += 1

MA = 0
count = 0
result = 0
for i in range(366):
    
    if graph[i] == 0:
        result += MA * count
        MA = 0
        count = 0
    else:
        MA = max(graph[i], MA)
        count += 1
    
result += MA * count

print(result)