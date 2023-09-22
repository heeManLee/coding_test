n = input()

temp = int(n[0])
count_0 = 0
count_1 = 0

if n[0] == '1':
    count_0 += 1
else:
    count_1 += 1

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        if n[i+1] == '1':
            count_0 += 1
        else:
            count_1 += 1


print(min(count_0, count_1))