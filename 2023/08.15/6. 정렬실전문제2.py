n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

result = sorted(array, reverse=True)

for i in range(n):
    print(result[i], end=' ')