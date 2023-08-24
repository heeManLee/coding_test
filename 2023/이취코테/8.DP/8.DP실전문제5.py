n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

DP = [10001] * (m+1)

DP[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if DP[j-array[i]] != 10001:
            DP[j] = min(DP[j-array[i]] + 1, DP[j])

if DP[m] == 10001:
    print(-1)
else:
    print(DP[m])