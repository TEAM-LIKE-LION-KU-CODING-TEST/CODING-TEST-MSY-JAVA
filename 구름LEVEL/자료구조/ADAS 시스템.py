import heapq

w, h = map(int, input().split())
directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
priority = {"E": 3, "P": 2, "0": 1}
sys_map = []
check = [[0 for _ in range(h)] for _ in range(w)]
stY = 0
stX = 0
for i in range(w):
    sys_map.append(input())
    if "S" in sys_map[i]:
        stY = i
        stX = sys_map[i].index("S")


def is_out(y, x):
    if y < 0 or y >= w or x < 0 or x >= h:
        return True
    return False


def danger_count(y, x, type):
    if type == "S" or type == "E":
        return 0
    danger_score = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            nowY = y - i
            nowX = x - j
            if nowY == y and nowX == x:
                continue
            if is_out(nowY, nowX):
                continue
            if sys_map[nowY][nowX] == "P":
                danger_score += 1
    if type == "P":
        danger_score -= 3
    return danger_score


def adas_drive(stY, stX):
    score = 0
    pq = []

    check[stY][stX] = -1
    for d in directions:
        nextY = stY + d[0]
        nextX = stX + d[1]
        if is_out(nextY, nextX):
            continue
        next_type = sys_map[nextY][nextX]
        heapq.heappush(pq, (-priority[next_type], nextY, nextX, next_type))
        check[nextY][nextX] = -1

    while pq:
        # 전체 후보군 중에서 가장 우선순위가 높은 정점
        p, y, x, type = heapq.heappop(pq)
        score += danger_count(y, x, type)
        if type == "E":
            break
        for d in directions:
            nextY = y + d[0]
            nextX = x + d[1]
            if is_out(nextY, nextX) or check[nextY][nextX] == -1:
                continue
            next_type = sys_map[nextY][nextX]
            heapq.heappush(pq, (-priority[next_type], nextY, nextX, next_type))
            check[nextY][nextX] = -1
    return max(0, score)

print(adas_drive(stY, stX))