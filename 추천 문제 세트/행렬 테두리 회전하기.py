def solution(rows, columns, queries):
    answer = []
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = cnt
            cnt += 1
    
    for q in queries:
        y1, x1 = q[0] - 1, q[1] - 1
        y2, x2 = q[2] - 1, q[3] - 1
        min_value = float('inf')
        
        d_mode = 0
        sY, sX = y1, x1
        rot_list = []
        while d_mode <= 3:
            min_value = min(min_value, board[sY][sX])
            nY = sY + directions[d_mode][0]
            nX = sX + directions[d_mode][1]
            if not ((y1 <= nY <= y2) and (x1 <= nX <= x2)):
                d_mode += 1
                continue
            rot_list.append([nY, nX, board[nY][nX]])
            sY = nY
            sX = nX
        
        # 일괄 회전 적용
        for i in range(len(rot_list)):
            y1, x1, num1 = rot_list[i]
            y2, x2, num2 = rot_list[(i + 1) % len(rot_list)]
            board[y2][x2] = num1

        # for b in board:
        #     print(b)
        
        answer.append(min_value)
    return answer