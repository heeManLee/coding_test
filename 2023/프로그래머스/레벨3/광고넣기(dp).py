# https://school.programmers.co.kr/learn/courses/30/lessons/72414

## dp문제.. 최적의 광고 넣는 알고리즘.. zfill 하면 시간 형태로 맞춰줄 수 있다

def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    all_time = [0 for i in range(play_time + 1)]
    
    for l in logs:
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        
        all_time[start] += 1
        all_time[end] -= 1
        
    for i in range(1, play_time):
        all_time[i] = all_time[i] + all_time[i-1]
    
    for i in range(1, play_time):
        all_time[i] = all_time[i] + all_time[i-1]    
    
    answer = 0
    max_time = -1
    for i in range(adv_time - 1, play_time):
        temp = all_time[i] - all_time[i - adv_time]
        if temp > max_time:
            max_time = temp
            answer = i - adv_time + 1
            
    return int_to_str(answer)
        
def int_to_str(time):
    h = str(time // 3600).zfill(2)
    m = str(time % 3600 // 60).zfill(2)
    s = str(time % 3600 % 60).zfill(2)
    
    return h + ":" + m + ":" + s


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)