def solution(name):
    # 상하 조작 횟수 계산
    alpha_cnt = 0
    for char in name:
        alpha_cnt += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 좌우 이동 횟수 계산 (최솟값)
    n = len(name)
    # 기본값 : 끝까지 쭉 오른쪽으로 가는 경우
    min_move = n - 1
    
    for i in range(n):
        # 현재 위치 i 다음으로 오는 연속된 'A'의 끝 지점(next_i) 찾기
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        # 1. 기존 값 (직진)
        # 2. 오른쪽으로 가다 왼쪽으로 꺾기 (i*2 + n-next_idx)
        # 3. 왼쪽으로 먼저 가다 오른쪽으로 꺾기 ((n-next_idx)*2 + i)
        min_move = min(min_move, i + i + n - next_idx, (n - next_idx) * 2 + i)
        
    return alpha_cnt + min_move