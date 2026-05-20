from collections import deque

def is_out_map(y, x, n, m):
    if y < 0 or x < 0 or y >= n or x >= m:
        return True
    return False

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    q = deque([])
    check = [[-1 for _ in range(m)] for _ in range(n)]
    dir = [[0, 1],[0, -1],[1, 0],[-1, 0]]
    
    check[0][0] = 1
    # (y, x)
    q.append([0, 0])
    while q:
        now = q.popleft()
        cur_y = now[0]
        cur_x = now[1]
        for d in dir:
            next_y = cur_y + d[0]
            next_x = cur_x + d[1]
            if is_out_map(next_y, next_x, n, m):
                continue
            if maps[next_y][next_x] == 0 or check[next_y][next_x] != -1:
                continue
            # 이전경로의 거리에서 1 더한 값을 현재 check에 기록
            check[next_y][next_x] = check[cur_y][cur_x] + 1
            q.append([next_y, next_x])
    
    answer = check[n - 1][m - 1]
    return answer