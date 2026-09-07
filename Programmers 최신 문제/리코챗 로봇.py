from collections import deque

def solution(board):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    rY, rX, gY, gX = 0, 0, 0, 0
    for i, line in enumerate(board):
        for j, l in enumerate(line):
            if l == "R":
                rY = i
                rX = j
            elif l == "G":
                gY = i
                gX = j

    def is_end(y, x):
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
            return True
        elif board[y][x] == "D":
            return True
        return False
    
    def slide(y, x, d):
        while not is_end(y, x):
            y += d[0]
            x += d[1]
        y -= d[0]
        x -= d[1]
        return y, x
    
    q = deque([])
    # 슬라이드 경로가 아닌, 슬라이드를 완료하고 도착한 위치가 check 기준위치
    check = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    q.append([rY, rX, 0])
    check[rY][rX] = True

    while q:
        y, x, cnt = q.popleft()
        for d in directions:
            nextY, nextX = slide(y, x, d)
            if check[nextY][nextX]:
                continue
            elif board[nextY][nextX] == "G":
                return cnt + 1
            q.append([nextY, nextX, cnt + 1])
            check[nextY][nextX] = True
    
    return -1