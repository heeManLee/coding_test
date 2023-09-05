import heapq

n = int(input())

q = []

for i in range(n):
    data = int(input())
    heapq.heappush(q, data)

result = 0

while len(q) != 1:
    one = heapq.heappop(q)
    two = heapq.heappop(q)

    sum_value = one + two
    result += sum_value
    heapq.heappush(q, sum_value)

print(result)