def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    # 시작 및 종료 시간을 총 초 단위로 변환
    start_sec = h1 * 3600 + m1 * 60 + s1
    end_sec = h2 * 3600 + m2 * 60 + s2
    
    # 시작 시간에 이미 초침이 시침이나 분침과 딱 맞아떨어져 있는지 확인 (시작 순간 알람 누락 방지)
    s_deg = (start_sec * 6) % 360
    m_deg = (start_sec * 0.1) % 360
    h_deg = (start_sec * (1 / 120)) % 360
    
    if s_deg == m_deg or s_deg == h_deg:
        answer += 1

    # 1초씩 진행하며 시뮬레이션
    for t in range(start_sec, end_sec):
        # 현재 시간의 바늘 위치 (0 ~ 360도 범위)
        cur_s = (t * 6) % 360
        cur_m = (t * 0.1) % 360
        cur_h = (t * (1 / 120)) % 360
        
        # 1초 뒤의 바늘 위치
        # 단, 360도 한 바퀴를 넘는 추월 순간 판별을 위해 % 360 이전 값(또는 360 처리)을 활용
        next_s = ((t + 1) * 6) % 360
        next_m = ((t + 1) * 0.1) % 360
        next_h = ((t + 1) * (1 / 120)) % 360
        
        # 360도 경계를 넘어가는 순간(0도가 되는 시점)의 예외 보정
        if next_s == 0: next_s = 360
        if next_m == 0: next_m = 360
        if next_h == 0: next_h = 360

        # 1초 사이 초침이 시침을 지나쳤는가?
        h_passed = (cur_s < cur_h) and (next_s >= next_h)
        
        # 1초 사이 초침이 분침을 지나쳤는가?
        m_passed = (cur_s < cur_m) and (next_s >= next_m)

        # 알람 카운트
        if h_passed and m_passed:
            # 1초 뒤 시침과 분침 위치가 동일하여 동시에 겹친 경우 (12시 정각 등) 1만 증가
            if next_h == next_m:
                answer += 1
            else:
                answer += 2
        elif h_passed or m_passed:
            answer += 1

    return answer