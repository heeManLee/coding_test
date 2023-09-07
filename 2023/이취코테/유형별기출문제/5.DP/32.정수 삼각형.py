n = int(input())

array = []
# array = []
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(array[i])):
        if j == 0:
            array[i][j] = array[i-1][j] + array[i][j]
        elif j == len(array[i]) - 1:
            array[i][j] = array[i-1][j-1] + array[i][j]
        else:
            array[i][j] = max(array[i][j] + array[i-1][j-1], array[i][j] + array[i-1][j])

print(max(array[n-1]))