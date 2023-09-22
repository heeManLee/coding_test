n, m = map(int, input().split())

graph = list(map(int, input().split()))

result = 0
lmax = -1
rmax = 0
for k in range(1, n+1):
    lmax = -1
    for i in range(m):
        if graph[i] >= k:
            if lmax == -1:
                lmax = i
            else:
                rmax = i
                result += (rmax - lmax - 1)
                lmax = rmax
                
                continue

print(result)