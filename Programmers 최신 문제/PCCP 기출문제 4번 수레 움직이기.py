import sys
sys.setrecursionlimit(200000)

# DFS 백트래킹
def solution(maze):
    answer = float('inf')
    N, M = len(maze), len(maze[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # 1 : 빨강, 2 : 파랑
    y1, x1, y2, x2 = 0, 0, 0, 0
    ye1, xe1, ye2, ye2 = 0, 0, 0, 0
    visited_red = [[False for _ in range(4)] for _ in range(4)]
    visited_blue = [[False for _ in range(4)] for _ in range(4)]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                y1, x1 = i, j
            elif maze[i][j] == 2:
                y2, x2 = i, j
            elif maze[i][j] == 3:
                ye1, xe1 = i, j
            elif maze[i][j] == 4:
                ye2, xe2 = i, j
    
    def backtrack(r1, c1, r2, c2, turn_count):
        nonlocal answer
        red_arrived = (r1, c1) == (ye1, xe1)
        blue_arrived = (r2, c2) == (ye2, xe2)
        
        if red_arrived and blue_arrived:
            answer = min(answer, turn_count)
            return
        
        red_next_list = []
        blue_next_list = []
        if red_arrived:
            red_next_list = [[r1, c1]]
        else:
            for d in directions:
                n_r1, n_c1 = r1 + d[0], c1 + d[1]
                if 0 <= n_r1 < N and 0 <= n_c1 < M:
                    if maze[n_r1][n_c1] != 5 and not visited_red[n_r1][n_c1]:
                        red_next_list.append([n_r1, n_c1])
        
        if blue_arrived:
            blue_next_list = [[r2, c2]]
        else:
            for d in directions:
                n_r2, n_c2 = r2 + d[0], c2 + d[1]
                if 0 <= n_r2 < N and 0 <= n_c2 < M:
                    if maze[n_r2][n_c2] != 5 and not visited_blue[n_r2][n_c2]:
                        blue_next_list.append([n_r2, n_c2])
        
        # 동시에 움직이는 것은 경우의 수 배열 Product 검사로 구현
        for n_r1, n_c1 in red_next_list:
            for n_r2, n_c2 in blue_next_list:
                # 동시에 같은 칸으로 이동하는지 체크
                if n_r1 == n_r2 and n_c1 == n_c2:
                    continue

                # 서로 자리를 바꿔서 교차하는지 체크
                if (n_r1, n_c1) == (r2, c2) and (n_r2, n_c2) == (r1, c1):
                    continue

                # 도착하지 않은 수레만 방문 표시
                if not red_arrived: visited_red[n_r1][n_c1] = True
                if not blue_arrived: visited_blue[n_r2][n_c2] = True

                # 다음 턴 DFS 호출
                backtrack(n_r1, n_c1, n_r2, n_c2, turn_count + 1)

                # 방문 표시 원복
                if not red_arrived: visited_red[n_r1][n_c1] = False
                if not blue_arrived: visited_blue[n_r2][n_c2] = False
        
    visited_red[y1][x1] = True
    visited_blue[y2][x2] = True
    backtrack(y1, x1, y2, x2, 0)
    
    if type(answer) == float:
        return 0
    return answer