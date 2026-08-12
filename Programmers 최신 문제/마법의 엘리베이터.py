def solution(storey):
    answer = 0
    list_y = list(map(int, str(storey)))
    
    idx = len(list_y) - 1
    
    while idx >= 0:
        now = list_y[idx]
        
        if now > 5:
            # 5 초과일 경우 올림
            answer += 10 - now
            if idx > 0:
                list_y[idx - 1] += 1
            else:
                # 최상위 자릿수에서 올림이 발생한 경우
                answer += 1
        elif now == 5:
            # 5일 경우 다음 상위 자릿수가 5 이상이면 올림 아니면 버림
            if idx > 0 and list_y[idx - 1] >= 5:
                answer += 5
                list_y[idx - 1] += 1
            else:
                answer += 5
        else:
            # 5 미만일 경우 버림
            answer += now
            
        idx -= 1
        
    return answer