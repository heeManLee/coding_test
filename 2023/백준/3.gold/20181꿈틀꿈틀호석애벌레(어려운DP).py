import sys
input = sys.stdin.readline
n, k = map(int, input().split())
array = list(map(int, input().split()))

dp = [0] * n
imax, ans = 0, 0

tmp = 0
left, right = 0, 0

while True:
    if tmp >= k:
        if left == 0:
            imax = 0
        else:
            imax = max(imax, dp[left-1])
        dp[right-1] = max(dp[right-1], imax + tmp - k)
        tmp -= array[left]
        left += 1
    elif right == n:
        break
    else:
        tmp += array[right]
        right += 1

for i in range(n):
    ans = max(ans, dp[i])

print(ans)