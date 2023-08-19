input_data = input()

y = int(input_data[1])
x = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2,1), (-1 ,2), (-1, -2), (1, 2), (1,-2)]

count = 0

for step in steps:
    ny = y + step[0]
    nx = x + step[1]

    if ny < 1 or ny > 8 or nx < 1 or nx > 8:
        continue
    count+=1

print(count)