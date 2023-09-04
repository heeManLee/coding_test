n = int(input())

num = list(map(int, input().split()))

plus, minus, multi, divide = map(int, input().split())

result_max = -1000000001
result_min = 1000000001

def go(pl, mi, mul, div, idx, now):
    global result_max
    global result_min
    if pl > plus or mi > minus or mul > multi or div > divide or idx > len(num):
        return
    
    if  pl == plus and mi == minus and mul == multi and div == divide:
        result_max = max(result_max, now)
        result_min = min(result_min, now)
        return

    go(pl+1, mi, mul, div, idx+1, now+num[idx])
    go(pl, mi+1, mul, div, idx+1, now-num[idx])
    go(pl, mi, mul+1, div, idx+1, now*num[idx])
    go(pl, mi, mul, div+1, idx+1, int(now/num[idx]))




go(0, 0, 0, 0, 1, num[0])


print(int(result_max))
print(int(result_min))