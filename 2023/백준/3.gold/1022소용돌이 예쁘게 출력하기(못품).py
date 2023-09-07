# 1 -> +1 중앙(1,1) 끝(2,2), 2-> +2 (2,2) 끝(4,4), 3-> +3 (3,3)
import sys

input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

y1, x1, y2, x2 = map(int, input().split())

board = [[0] * ((x2 - x1) + 1) for _ in range((y2-y1) + 1)]
number_of_board = (x2-x1+1) * (y2-y1+1)

y = 0
x = 0
num = 1
count = 0
dcnt = 1
d = 0

while number_of_board > 0:
    if y1 <= y <= y2 and x1 <= x <= x2:
        number_of_board -= 1
        board[y - y1][x- x1] = num
        max_num = num
    num += 1
    count += 1

    y = y + dy[d]
    x = x + dx[d]

    if count == dcnt:
        count = 0
        d = (d + 3) % 4
        if d == 0 or d == 2:
            dcnt += 1


# #### map을 사용해서 최대값 구하기!!
# temp_result_max = max(map(max, temp_result))

max_len = len(str(max_num-1))

for i in range(y2-y1+1):
    for j in range(x2-x1+1):
        print(str(board[i][j]).rjust(max_len), end=' ')
    print()

# for i in range(len(temp_result)):
#     for j in range(len(temp_result[0])):
#         if len(str(temp_result[i][j])) != max_len:
#             str_temp = ""
#             for k in range(max_len - len(str(temp_result[i][j]))):
#                 str_temp += " "
#             str_temp += str(temp_result[i][j])
#             print(str_temp, end=' ')
#         else:
#             print(str(temp_result[i][j]), end=' ')
#     print("")