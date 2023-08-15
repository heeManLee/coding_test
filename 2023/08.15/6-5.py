## 파이썬 자체 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
result.sort()



array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)