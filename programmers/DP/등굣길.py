def solution(m, n, puddles):
    # 왼쪽, 위쪽에서 오는 방향만
    direction = [[0, -1], [-1, 0]]
    route = [[0 for _ in range(m)] for _ in range(n)]
    for p in puddles:
        # 물 웅덩이는 -1로 표시
        route[p[1] - 1][p[0] - 1] = -1
    
    # 시작점 설정
    route[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            # 물 웅덩이거나 시작점이면 연산 건너뛰기
            if route[i][j] == -1 or (i == 0 and j == 0):
                continue
            # direction을 순회하며 경로 합산
            count = 0
            for d in direction:
                prevY = i + d[0]
                prevX = j + d[1]
                if 0 <= prevY < n and 0 <= prevX < m and route[prevY][prevX] != -1:
                    count += route[prevY][prevX]            
            route[i][j] = count % 1000000007
    
    return route[n-1][m-1]