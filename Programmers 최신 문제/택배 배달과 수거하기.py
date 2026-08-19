def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx = n - 1
    p_idx = n - 1
    
    # 초기 각 최대 배달/수거 위치 찾기
    while d_idx >= 0 and deliveries[d_idx] == 0:
        d_idx -= 1
    while p_idx >= 0 and pickups[p_idx] == 0:
        p_idx -= 1
    
    while True:
        if d_idx < 0 and p_idx < 0:
            break
        now_cap = cap
        idx = max(d_idx, p_idx) + 1
        # 최대 위치까지 가면서 무조건 cap만큼 멀리서부터 배달
        while now_cap > 0 and d_idx >= 0:
            if deliveries[d_idx] <= now_cap:
                now_cap -= deliveries[d_idx]
                deliveries[d_idx] = 0
                d_idx -= 1
            else:
                deliveries[d_idx] -= now_cap
                now_cap = 0
        while d_idx >= 0 and deliveries[d_idx] == 0:
            d_idx -= 1
        # 최대 위치에서 오면서 무조건 cap만큼 멀리서부터 수거
        p_cap = cap
        while p_idx >= 0 and p_cap > 0:
            if pickups[p_idx] <= p_cap:
                p_cap -= pickups[p_idx]
                pickups[p_idx] = 0
                p_idx -= 1
            else:
                pickups[p_idx] -= p_cap
                p_cap = 0
        while p_idx >= 0 and pickups[p_idx] == 0:
            p_idx -= 1
        answer += idx * 2
    return answer