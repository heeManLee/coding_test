def solution(a, b, g, s, w, t):
    answer = (10 ** 9) * 2 * (10 ** 5) * 2
    start = 0
    ## 최악의 경우, 도시 1개 금 10^9, 은10^9, 왕복시간 10^5
    end = (10 ** 9) * 2 * (10 ** 5) * 2
    
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0
        
        # 주어진 시간내에 이동할 수 있는 횟수
        for i in range(len(g)):
            now_gold = g[i]
            now_silver = s[i]
            now_time = t[i]
            now_weight = w[i]
            move_cnt = mid // (now_time * 2)
            
            if mid % (now_time * 2) >= now_time:
                move_cnt += 1
            
            ## 최대 적재량 구하기
            possible_move_weight = move_cnt * now_weight
            
            ## 주어진 시간 내 최대 적재 가능량 누적하기
            if now_gold < possible_move_weight:
                gold += now_gold
            else:
                gold += possible_move_weight
                
            if now_silver < possible_move_weight:
                silver += now_silver
            else:
                silver += possible_move_weight
                
            if now_gold + now_silver < possible_move_weight:
                total += now_gold + now_silver
            else:
                total += possible_move_weight
            
        if gold >= a and silver >= b and total >= a+b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    
    
    return answer