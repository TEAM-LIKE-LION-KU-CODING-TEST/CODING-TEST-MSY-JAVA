import copy
# 최악의 경우 200(최대 단일 이동 루트 거리) x 100(루트 개수) x (100(로봇 개수) + 100(전체 맵 검사))
def solution(points, routes):
    answer = 0
    # 로봇 번호는 0번부터 시작
    robot_alive = set([])
    # 현재 y, x, dst point
    cur_pos = []
    # 1 ~ 100까지의 좌표
    maps = [[set([]) for _ in range(102)] for _ in range(102)]
    
    for i, r in enumerate(routes):
        robot_alive.add(i)
        cur_pos.append(copy.deepcopy(points[r[0] - 1]))
        maps[cur_pos[i][0]][cur_pos[i][1]].add(i)
        cur_pos[i].append(1)
    
    def next_move(y, x, dst):
        dy, dx = points[dst - 1]
        if y == dy and x == dx:
            return [0, 0]
        if y != dy:
            if y < dy:
                return [1, 0]
            else:
                return [-1, 0]
        else:
            if x < dx:
                return [0, 1]
            else:
                return [0, -1]
    
    def cnt_collison():
        result = 0
        for i in range(1, 101):
            for j in range(1, 101):
                if len(maps[i][j]) > 1:
                    result += 1
        return result
    
    answer += cnt_collison()
    while len(robot_alive) > 0:
        moves = []
        for i in list(robot_alive):
            y, x, dst = cur_pos[i]
            
            if dst >= len(routes[i]):
                maps[y][x].remove(i)
                robot_alive.remove(i)
                continue
                
            add_y, add_x = next_move(y, x, routes[i][dst])
            
            if add_y == 0 and add_x == 0:
                cur_pos[i][2] += 1
                if cur_pos[i][2] >= len(routes[i]):
                    maps[y][x].remove(i)
                    robot_alive.remove(i)
                    continue
                add_y, add_x = next_move(y, x, routes[i][cur_pos[i][2]])
                
            moves.append((i, y, x, add_y, add_x))
            
        for i, y, x, add_y, add_x in moves:
            maps[y][x].remove(i)
            cur_pos[i][0] += add_y
            cur_pos[i][1] += add_x
            maps[cur_pos[i][0]][cur_pos[i][1]].add(i)
            
        if len(robot_alive) > 0:
            answer += cnt_collison()
    
    return answer