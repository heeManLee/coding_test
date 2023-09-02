#### 1~10 까지 범위가 정해져 있는거는 리스트를 만들어서 넣자
n, m = map(int, input().split())
array = list(map(int, input().split()))

ball = [0] * 11

for i in array:
    ball[i] += 1

result = 0
for i in range(1, m+1):
    n -= ball[i]
    result += ball[i] * n

print(result)