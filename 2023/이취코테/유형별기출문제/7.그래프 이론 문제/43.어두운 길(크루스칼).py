def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())

edges = []

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

total = 0
for i in range(m):
    a, b, cost = map(int, input().split())
    total += cost
    edges.append((cost, a, b))

edges.sort()

result = 0
for i in range(len(edges)):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union(parent, a, b)

print(total - result)