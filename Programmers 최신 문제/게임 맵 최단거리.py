from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque([])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    check = [[-1 for _ in range(m)] for _ in range(n)]
    
    def is_out(y, x):
        if y < 0 or y >= n or x < 0 or x >= m:
            return True
        return False
    
    # (y, x)
    q.append([0, 0])
    check[0][0] = 1
    while q:
        y, x = q.popleft()
        for d in directions:
            ny = y + d[0]
            nx = x + d[1]
            if is_out(ny, nx) or maps[ny][nx] == 0 or check[ny][nx] != -1:
                continue
            check[ny][nx] = check[y][x] + 1
            q.append([ny, nx])
    
    # for c in check:
    #     print(c)
    
    return check[n - 1][m - 1]