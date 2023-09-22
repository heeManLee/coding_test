n = input()

result = ['']*len(n)

def go(arr, start):
    if not arr:
        return
    
    MI = min(arr)
    idx = 0
    for i in range(len(arr)):
        if arr[i] == MI:
            idx = i
            break
    result[start+idx] = MI
    print("".join(result))
    go(arr[idx+1:], start+idx+1)
    go(arr[:idx], start)

go(n, 0)