## 슬라이싱을 위한 인덱스를 구분할 때 생각을 최대한 잘 해야한다.

n = input()

MA = -1
MI = 10000000

def go(count, num):
    global MA
    global MI
    if len(num) == 1:
        if int(num) % 2 == 1:
            count += 1
        MA = max(count, MA)
        MI = min(count, MI)
        return
    elif len(num) == 2:
        for i in range(2):
            if int(num[i]) % 2 == 1:
                count += 1
        go(count, str(int(num[0]) + int(num[1])))
    else:
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                count += 1
        for i in range(1, len(num)-1):
            for j in range(i+1, len(num)):
                go(count, str(int(num[:i]) + int(num[i:j]) + int(num[j:])))
        

go(0, n)

print(str(MI) + " " + str(MA))