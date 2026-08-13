import sys
# 재귀 사용시 반드시 limit 늘려주기
sys.setrecursionlimit(1000000)

def solution(n, m, x, y, r, c, k):
    # d > l > r > u
    keys = ['d', 'l', 'r', 'u']
    directions = [[1, 0], [0, -1], [0, 1], [-1, 0]]
    
    answer = ''
    x_diff = r - x
    y_diff = c - y
    
    if (k - (abs(x_diff) + abs(y_diff))) % 2 != 0:
        return "impossible"
    if k < (abs(x_diff) + abs(y_diff)):
        return "impossible"
    
    def is_out(x, y):
        if x < 1 or x > n or y < 1 or y > m:
            return True
        return False
    
    route = []
    def find_route(now_x, now_y, cnt, rou):
        if cnt == k and now_x == r and now_y == c:
            return ''.join(rou)
        elif cnt == k:
            return False
        
        for i, d in enumerate(directions):
            next_x = now_x + d[0]
            next_y = now_y + d[1]
            if is_out(next_x, next_y):
                continue
            # 가지치기를 통해 최적화 및 그리디의 정당성 부여
            if (k - (cnt + 1)) < (abs(r - next_x) + abs(c - next_y)):
                continue
            rou.append(keys[i])
            result = find_route(next_x, next_y, cnt + 1, rou)
            if result != False:
                return result
            rou.pop()
    
    answer = find_route(x, y, 0, route)
    return answer