from collections import deque

def solution(maps):
    answer = 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    def find(pos):
        for i, m in enumerate(maps):
            for j, now in enumerate(m):
                if now == pos:
                    return i, j
    
    def is_out(y, x):
        if y < 0 or y >= len(maps) or x < 0 or x >= len(maps[0]):
            return True
        return False
    
    def bfs(stY, stX, edY, edX):
        q = deque([])
        check = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
        check[stY][stX] = True
        q.append([stY, stX, 0])
        while q:
            nowY, nowX, cnt = q.popleft()
            for d in directions:
                nextY = nowY + d[0]
                nextX = nowX + d[1]
                if is_out(nextY, nextX):
                    continue
                if check[nextY][nextX] or maps[nextY][nextX] == "X":
                    continue
                if nextY == edY and nextX == edX:
                    return cnt + 1
                check[nextY][nextX] = True
                q.append([nextY, nextX, cnt + 1])
        return -1
    
    # 레버로 향하는 최단거리 우선 계산
    stY, stX = find("S")
    edY, edX = find("L")
    lever = bfs(stY, stX, edY, edX)
    if lever == -1:
        return -1
    answer += lever
    
    # 이후 레버에서 출구까지의 최단거리 계산
    stY, stX = find("L")
    edY, edX = find("E")
    exit = bfs(stY, stX, edY, edX)
    if exit == -1:
        return -1
    answer += exit
    
    return answer