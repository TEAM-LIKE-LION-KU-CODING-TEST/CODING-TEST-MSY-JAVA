from collections import deque

def solution(maps):
    answer = []
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    def is_out(y, x):
        if y < 0 or y >= len(maps) or x < 0 or x >= len(maps[0]):
            return True
        return False
    
    check = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    def bfs(stY, stX):
        food = 0
        q = deque([])
        q.append([stY, stX])
        while q:
            nowY, nowX = q.popleft()
            food += int(maps[nowY][nowX])
            for d in directions:
                nextY = nowY + d[0]
                nextX = nowX + d[1]
                if is_out(nextY, nextX):
                    continue
                if maps[nextY][nextX] == "X" or check[nextY][nextX] == 1:
                    continue
                q.append([nextY, nextX])
                check[nextY][nextX] = 1
        return food
        
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and check[i][j] == 0:
                check[i][j] = 1
                answer.append(bfs(i, j))
    
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer