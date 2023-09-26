### 아쉬웠던 점:
### split(' ')에 대한 확신 -> 그냥 그 결과 자체가 리스트임, 
### 딕셔너리에 키 값이 있는지 확인하려면 a in out 으로 하면 됨
### 문제 있는 조건으로 판단식을 해야한다.

def solution(fees, records):
    answer = []
    out_time = 60 * 23 + 59
    
    out = {}
    now = []
    for i in range(len(records)):
        temp_list = records[i].split(' ')
        if temp_list[2] == "IN":
            now.append([int(temp_list[0][:2]) * 60 + int(temp_list[0][3:]), temp_list[1]])
        else:
            temp_out_time = int(temp_list[0][:2]) * 60 + int(temp_list[0][3:])
            for i in range(len(now)):   
                if temp_list[1] == now[i][1]:
                    if temp_list[1] in out:
                        out[temp_list[1]] += temp_out_time - now[i][0]
                        now.remove([now[i][0], now[i][1]])
                        break
                    else:
                        out[temp_list[1]] = temp_out_time - now[i][0]
                        now.remove([now[i][0], now[i][1]])
                        break
    
    if now:
        for i in range(len(now)):
            if now[i][1] in out:
                out[now[i][1]] += out_time - now[i][0]
            else:
                out[now[i][1]] = out_time - now[i][0]
    
    bill = []
    for i in out.keys():
        if out[i] <= fees[0]:
            bill.append([i, fees[1]])
        else:
            time = 0
            temp_time = out[i] - fees[0]
            if temp_time % fees[2] != 0:
                time = 1
            time += temp_time // fees[2]

            bill.append([i, fees[1]+ time * fees[3]])
    
    bill.sort()

    for i in range(len(bill)):
        answer.append(bill[i][1])      
    
    return answer

solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])