temp_max = 0
def cal(idx, x, n):
    global temp_max
    if (idx == len(n)-1):
        if x > temp_max:
            temp_max = x
            return
        return
    
    cal(idx+1, x + int(n[idx+1]), n)
    cal(idx+1, x * int(n[idx+1]), n)



n = input()

cal(0, int(n[0]), n)

print(temp_max)
