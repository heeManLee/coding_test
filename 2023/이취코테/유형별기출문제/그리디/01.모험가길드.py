n = int(input())

array = list(map(int, input().split()))

result = 0
count = 0
array.sort()
for i in array:
    count += 1
    if count >= i:
        result+=1
        count = 0

print(result)

