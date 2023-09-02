n = input()

temp = int(n[0])
count_0 = 0
count_1 = 0
for i in range(1, len(n)):
    if temp != int(n[i]):
        if temp == 0:
            count_0 += 1
        elif temp == 1:
            count_1 += 1
        temp = int(n[i])

print(min(count_0, count_1))