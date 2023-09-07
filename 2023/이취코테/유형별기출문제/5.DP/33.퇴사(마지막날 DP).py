## 퇴사하는 날 받는 돈이므로 마지막에 한 칸을 추가 해줘야 한다.
import sys

n = int(input())

array = []
result = 0


for i in range(n):
    t, p = map(int, input().split())
    array.append([t,p])

array.append([0,0])

dp = [0 for i in range(n+1)]

for i in range(n):
    dp[i] = max(dp[i], array[i][1])
    for j in range(i + array[i][0], n+1):
        if dp[j] < dp[i] + array[j][1]:
            dp[j] = dp[i] + array[j][1]

print(dp[-1])