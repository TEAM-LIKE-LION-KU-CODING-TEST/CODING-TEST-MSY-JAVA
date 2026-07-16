from collections import deque

def get_1d_sliding_min(arr, k):
    # 1차원 배열 arr에서 길이가 k인 슬라이딩 윈도우의 최솟값 배열 반환
    n = len(arr)
    if n < k: 
        return []
    
    result = []
    q = deque()
    
    for i in range(n):
        # 윈도우 범위를 벗어난 인덱스 제거
        if q and q[0] <= i - k:
            q.popleft()
        # 현재 값보다 큰 값들을 deque의 뒤에서부터 제거
        while q and arr[q[-1]] >= arr[i]:
            q.pop()
        # 현재 인덱스 추가
        q.append(i)
        # 윈도우가 가득 차면 결과에 최솟값(deque의 맨 앞 요소) 추가
        if i >= k - 1:
            result.append(arr[q[0]])
    return result

def solution(m, n, h, w, drops):
    # 격자 초기화 (비가 내리지 않는 곳은 무한대)
    grid = [[float('inf')] * n for _ in range(m)]
    for i, (r, c) in enumerate(drops):
        grid[r][c] = i + 1
        
    # 가로 방향 슬라이딩 윈도우 최솟값 계산
    row_min = []
    for i in range(m):
        row_min.append(get_1d_sliding_min(grid[i], w))
        
    # 세로 방향 슬라이딩 윈도우 최솟값 계산
    col_min = [[0] * (n - w + 1) for _ in range(m - h + 1)]
    for j in range(n - w + 1):
        # 각 열에 대해 1차원 배열 추출
        col_arr = [row_min[i][j] for i in range(m)]
        # 세로 방향 최소값 계산
        col_res = get_1d_sliding_min(col_arr, h)
        for i in range(m - h + 1):
            col_min[i][j] = col_res[i]
            
    # 가장 늦게 젖는 최적의 구역 찾기
    max_time = -1
    answer = [-1, -1]
    
    # 위쪽, 왼쪽 우선이므로 0부터 순회하며 갱신
    for i in range(m - h + 1):
        for j in range(n - w + 1):
            if col_min[i][j] > max_time:
                max_time = col_min[i][j]
                answer = [i, j]
                
    return answer