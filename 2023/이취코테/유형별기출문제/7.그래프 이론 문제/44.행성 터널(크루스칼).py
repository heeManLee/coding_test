import sys

input = sys.stdin.readline

n = int(input())
planet = []

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []

for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

result = 0
for i in range(len(edges)):
    cost, a, b = edges[i]
    if find(parent, a) != find(parent,b):
        union(parent, a, b)
        result += cost

print(result)