def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

g = int(input())
p = int(input())

parent = [0] * (g+1)

for i in range(g+1):
    parent[i] = i

result = 0
for i in range(p):
    plane = int(input())
    data = find_parent(parent, plane)
    if data == 0:
        break
    else:
        union_parent(parent, data, data-1)
        result+=1

print(result)