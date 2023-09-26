## 마지막에 처리해줄때 조건을 잘 확인해보자
## https://school.programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    answer = ''
    bus_h = 9
    bus_m = 0
    ## 버스 시간 처리
    bus_time = []
    for i in range(n):
        temp_h = ""
        temp_m = ""
        if bus_h < 10:
            temp_h = "0" + str(bus_h)
        else:
            temp_h = str(bus_h)
            
        if bus_m < 10:
            temp_m = "0" + str(bus_m)
        else:
            temp_m = str(bus_m)
        bus_time.append(temp_h+temp_m)
        bus_m += t
        if bus_m >= 60:
            bus_m -= 60
            bus_h += 1
    ##사람들 버스 타는 시간 처리
    people_time = []
    for i in range(len(timetable)):
        temp = timetable[i][:2] + timetable[i][3:5]
        people_time.append(temp)
    people_time.sort()
    
    ##콘이 마지막 visit
    visit = [0] * len(timetable)
    people_idx = 0
    
    ## 마지막 전 버스까지 몇 명이 탈 수 있는지
    for i in range(len(bus_time)-1):
        count = 0
        temp_idx = people_idx
        for k in range(temp_idx, len(people_time)):
            if count == m:
                break
            if int(people_time[k]) <= int(bus_time[i]) and visit[k] == 0:
                people_idx += 1
                visit[k] = 1
                count += 1
    ## 마지막 버스 처리, 콘은 마지막 탈 수 있는 위치에 넣어야 한다.
    ## 아직 못 탄 사람 명수 경우 1. 남은 사람이 용량보다 적으면 콘 자리도 있다.
    line_num = len(people_time) - people_idx
    
    if line_num < m or line_num == 0 or int(people_time[people_idx]) > int(bus_time[-1]):
        return str(bus_time[-1])[:2] + ":" + str(bus_time[-1][2:4])

    if n == 1 and bus_time[0] < people_time[people_idx]:
        return str(bus_time[0])[:2] + ":" + str(bus_time[0])[2:4]
    
    count = 0
    result_time = ""
    for k in range(people_idx, len(people_time)):
        if count == m - 1:
            con_time_h = int(people_time[k][:2])
            con_time_m = int(people_time[k][2:4])
            if con_time_m == 0:
                con_time_h -= 1
                con_time_m = 59
            else:
                con_time_m -= 1
            
            if con_time_h < 10:
                result_time += "0" + str(con_time_h) + ":"
            else:
                result_time += str(con_time_h) + ":"
                
            if con_time_m < 10:
                result_time += "0" + str(con_time_m)
            else:
                result_time += str(con_time_m)
            
            return result_time
        
        count += 1