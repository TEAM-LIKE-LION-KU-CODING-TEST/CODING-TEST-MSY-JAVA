def solution(board):
    # -1 : 아직 보드에 채워야 할 문자가 남음
    # 0 : 빈 공간, 1 : O, 2 : X
    check = [[-1 for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                check[i][j] = 0
    
    def is_end():
        # 가로
        for i in range(3):
            flag = True
            now = check[i][0]
            if now == -1 or now == 0:
                continue
            for j in range(1, 3):
                if check[i][j] != now:
                    flag = False
                    break
            if flag:
                return True
        
        # 세로
        for i in range(3):
            flag = True
            now = check[0][i]
            if now == -1 or now == 0:
                continue
            for j in range(1, 3):
                if check[j][i] != now:
                    flag = False
                    break
            if flag:
                return True
        
        # 대각선
        if check[0][0] != 0 and check[0][0] != -1 and check[0][0] == check[1][1] and check[1][1] == check[2][2]:
            return True
        if check[0][2] != 0 and check[0][2] != -1 and check[0][2] == check[1][1] and check[1][1] == check[2][0]:
            return True
        
        return False
        
    def is_left():
        for i in range(3):
            for j in range(3):
                if check[i][j] == -1:
                    return True
        return False
    
    char_li = ["O", "X"]
    def dfs(idx):
        # 보드에 있는 돌을 모두 시뮬레이션으로 채우는 데 성공했다면 유효한 판
        if not is_left():
            return True
        
        # 다 안 채워졌는데 벌써 게임이 끝났다면 이 순서는 무효
        if is_end():
            return False

        for i in range(3):
            for j in range(3):
                if board[i][j] == char_li[idx % 2] and check[i][j] == -1:
                    check[i][j] = idx % 2 + 1
                    
                    if dfs(idx + 1):
                        return True
                        
                    check[i][j] = -1
                    
        # 모든 경우를 다 해봐도 안 되면 실패
        return False

    if dfs(0):
        return 1
    else:
        return 0