def solution(order):
    answer = 0
    order_pos = 0
    # 보조 컨베이어 벨트
    sub = []
    # 1부터 순서대로 들어오는 상자
    # pop을 위해 역순 배열로 설정
    now = [i for i in range(len(order), 0, -1)]
    
    while sub or now:
        if now and now[-1] == order[order_pos]:
            now.pop()
            order_pos += 1
            answer += 1
            continue
        if sub and sub[-1] == order[order_pos]:
            sub.pop()
            order_pos += 1
            answer += 1
            continue
        if now and now[-1] != order[order_pos]:
            sub.append(now.pop())
            continue
        break
    
    return answer