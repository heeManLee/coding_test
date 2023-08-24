# n = int(input())
# array = list(map(int, input().split()))
# m = int(input())
# want = list(map(int, input().split()))

# count = 0

# def binaray_search(array, goal, start, end):
#     if start>end:
#         return False
    
#     mid = (start+end) // 2
#     if array[mid] == goal:
#         return True
#     elif array[mid] > goal:
#         end = mid-1
#     elif array[mid] < goal:
#         start = mid+1
    
#     return binaray_search(array, goal, start, end)

# array.sort()

# for i in range(len(want)):
#     if binaray_search(array, want[i], 0, n-1):
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

##########################

n = int(input())
array = set(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

for i in want:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
