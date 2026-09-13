from collections import deque


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])

    land_oil = [[[0, -1] for _ in range(m)] for _ in range(n)]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(y, x, group):
        q = deque([[y, x]])
        land_oil[y][x] = [0, group]
        cells = [(y, x)]

        while q:
            nowY, nowX = q.popleft()
            for dy, dx in directions:
                nextY, nextX = nowY + dy, nowX + dx
                # 범위 체크 및 미방문 석유 땅 확인
                if 0 <= nextY < n and 0 <= nextX < m:
                    if land[nextY][nextX] == 1 and land_oil[nextY][nextX][1] == -1:
                        # 큐 삽입 시 방문 처리
                        land_oil[nextY][nextX][1] = group
                        q.append([nextY, nextX])
                        cells.append((nextY, nextX))

        cnt = len(cells)
        for cy, cx in cells:
            land_oil[cy][cx][0] = cnt

    group = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and land_oil[i][j][1] == -1:
                bfs(i, j, group)
                group += 1

    for i in range(m):
        oil = 0
        cur = set()
        for j in range(n):
            if land_oil[j][i][0] > 0 and land_oil[j][i][1] not in cur:
                oil += land_oil[j][i][0]
                cur.add(land_oil[j][i][1])
        answer = max(answer, oil)

    return answer