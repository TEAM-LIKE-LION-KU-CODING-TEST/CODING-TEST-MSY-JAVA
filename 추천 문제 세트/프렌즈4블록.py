def solution(m, n, board):
    answer = 0
    # board_list로 ord를 통해 변환, -1은 빈칸
    board_list = []
    for i, b in enumerate(board):
        board_list.append([])
        for c in b:
            board_list[i].append(ord(c))
    box = [[0, 1], [1, 0], [1, 1]]
    
    def round_each():
        flag = False
        pop_list = set([])
        for x in range(n - 1):
            for y in range(m - 1):
                if board_list[y][x] == -1:
                    continue
                now_set = set([])
                now_set.add(tuple([y, x]))
                for b in box:
                    nY = y + b[0]
                    nX = x + b[1]
                    if board_list[nY][nX] == board_list[y][x]:
                        now_set.add(tuple([nY, nX]))
                if len(now_set) == 4:
                    pop_list = pop_list | now_set
                    flag = True
        pop_list = sorted(pop_list, key=lambda x : (x[1], -x[0]))
        return flag, pop_list
    
    while True:
        flag, pop_list = round_each()
        if not flag:
            break
        answer += len(pop_list)
        for p in pop_list:
            board_list[p[0]][p[1]] = -1
            
        # 각 열의 최 하단부터 -1 위치를 가장 가까운 블록으로 채우는 방식
        for x in range(n):
            idx = m - 1
            while True:
                if idx <= 0:
                    break
                if board_list[idx][x] == -1:
                    block_exist = False
                    block = idx - 1
                    while block >= 0:
                        if board_list[block][x] != -1:
                            board_list[idx][x] = board_list[block][x]
                            board_list[block][x] = -1
                            block_exist = True
                            break
                        block -= 1
                    if not block_exist:
                        break
                idx -= 1
    
    return answer