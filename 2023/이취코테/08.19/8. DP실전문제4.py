n = int(input())

DP = [0] * 1001

DP[1] = 1
DP[2] = 3

for i in range(3, n+1):
    DP[i] = (DP[i-2] * 2 + DP[i-1]) % 796796

print(DP[n])