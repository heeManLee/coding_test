n, x = map(int, input().split())

array = list(map(int, input().split()))

def find_count(array, goal):
    a = find_first(array, goal, 0, len(array)-1)

    if a == None:
        return 0
    
    b = find_end(array, goal, 0, len(array)-1)

    return b-a+1



def find_first(array, goal, start, end):
    if start>end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == goal and (mid == 0 or array[mid-1] < array[mid]):
        return mid
    elif array[mid] >= goal:
        return find_first(array, goal, start, mid-1)
    elif array[mid] < goal:
        return find_first(array, goal, mid+1, end)



def find_end(array, goal, start, end):
    global n
    if start>end:
        return False
    
    mid = (start+end) // 2

    if array[mid] == goal and (mid == n-1 or array[mid] < array[mid+1]):
        return mid
    elif array[mid] > goal:
        return find_end(array, goal, start, mid-1)
    else:
        return find_end(array, goal, mid+1, end)
    
count = find_count(array, x)

if count == 0:
    print(-1)
else:
    print(count)