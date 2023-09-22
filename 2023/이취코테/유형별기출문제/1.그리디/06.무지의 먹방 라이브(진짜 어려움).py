import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, [food_times[i], i+1])
    
    length = len(food_times)
    
    while q[0][0] * length <= k:
        now = heapq.heappop(q)[0]
        k -= now * length
        length -= 1
        for i in range(length):
            q[i][0] -= now
    
    result = sorted(q, key = lambda x: x[1])
    return result[k % length][1]

solution([8, 6, 4], 15)