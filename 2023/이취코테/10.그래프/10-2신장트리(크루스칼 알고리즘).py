###신장트리는 그래프의 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다.
###최소한의 비용으로 신장 트리를 찾는 알고리즘 (최소 신장 트리) : 크루스칼 알고리즘
###간선의 길이 오름차순, 사이클 발생하지 않으면 추가, 발생시키면 추가 X

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

v, e = map(int, input().split())
parent = [0] * (v + 1)
edges = []
result = 0

# 자기 자신을 루트로
for i in range(1, v+1):
    parent[i] = i


for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

#### 가격 순으로 정렬
edges.sort()

for edge in range(edges):
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)