from collections import deque

def solution(places):
    answer = []
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    def is_out(y, x):
        if y < 0 or y >= 5 or x < 0 or x >= 5:
            return True
        return False
    
    def bfs(stY, stX, p):
        # check 배열을 매 BFS 호출마다 독립적으로 생성
        check = [[False for _ in range(5)] for _ in range(5)]
        q = deque([])
        
        # (y, x, 출발점으로부터의 최단 이동 거리)
        q.append([stY, stX, 0])
        check[stY][stX] = True
        
        while q:
            y, x, dist = q.popleft()
            
            # 최단 거리가 이미 2이면 다음 칸은 무조건 거리 3 이상이므로 탐색 중단
            if dist == 2:
                continue
            
            for d in directions:
                nextY = y + d[0]
                nextX = x + d[1]
                if is_out(nextY, nextX) or check[nextY][nextX] or p[nextY][nextX] == "X":
                    continue
                    
                # 한 칸 이동했으므로 dist + 1이 최단 거리
                if p[nextY][nextX] == "P":
                    return False  # 거리 2 이하에서 사람을 만났으므로 즉시 탈락
                    
                q.append([nextY, nextX, dist + 1])
                check[nextY][nextX] = True
        return True
    
    for p in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if p[i][j] == "P":
                    if not bfs(i, j, p):
                        flag = 0
                        break
            if flag == 0:
                break
        answer.append(flag)
    return answer
