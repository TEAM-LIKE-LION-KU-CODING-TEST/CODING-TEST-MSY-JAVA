from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dir_val = [[1, 0],[-1, 0],[0, 1],[0, -1]]
    # 방문 테두리 : 2, 테두리 : 1, 내부 공간 : 0, 빈 공간 : -1
    geo = [[-1 for _ in range(102)] for _ in range(102)]
    
    # BFS 경로 건너뛰기 방지를 위해 모든 좌표 값 * 2
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    for r in rectangle:
        # 좌표 2배 확장
        x1, y1, x2, y2 = r[0] * 2, r[1] * 2, r[2] * 2, r[3] * 2
        # 테두리와 내부 매핑
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 직사각형 내부 공간인 경우
                if x1 < i < x2 and y1 < j < y2:
                    geo[j][i] = 0
                # 직사각형 테두리인 경우
                # 기존 값 0이 아닌 경우에만 1로 설정
                # 기존 값 0 = 다른 직사각형 내부
                elif geo[j][i] != 0:
                    geo[j][i] = 1
    
    q = deque([])
    q.append([characterY, characterX, 0])
    geo[characterY][characterX] = 2
    while q:
        now = q.popleft()
        now_y = now[0]
        now_x = now[1]
        now_cnt = now[2]
        if now_y == itemY and now_x == itemX:
            return now_cnt / 2
        for d in dir_val:
            next_y = now_y + d[0]
            next_x = now_x + d[1]
            if geo[next_y][next_x] == 1:
                geo[next_y][next_x] = 2
                q.append([next_y, next_x, now_cnt + 1])