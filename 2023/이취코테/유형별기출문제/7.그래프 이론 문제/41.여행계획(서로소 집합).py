def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * n


for i in range(n):
    parent[i] = i

con = []
for i in range(n):
    array = list(map(int, input().split()))
    for j in range(n):
        if array[j] == 1:
            con.append((i,j))

for i in con:
    a = i[0]
    b = i[1]
    if a >= b or find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union(parent, a, b)

        
goal_list = list(map(int, input().split()))

goal = find_parent(parent, goal_list[0])

flag = 1
for i in range(1, len(goal_list)):
    if goal != find_parent(parent, goal_list[i]):
        flag = 0
        break

if flag:
    print("YES")
else:
    print("NO")