n = input()
alpha = []
result = 0

for i in n:
    if i.isalpha():
        alpha.append(i)
    else:
        result += int(i)

alpha.sort()

if result != 0:
    alpha.append(str(result))

print(''.join(alpha))