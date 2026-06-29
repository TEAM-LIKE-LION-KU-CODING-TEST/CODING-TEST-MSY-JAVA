# BFS + Union Find
from collections import deque

year = 0
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n, k = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]
parent = [i for i in range(k + 1)]
q = deque([])
for i in range(k):
	x, y = map(int, input().split())
	board[y - 1][x - 1] = i + 1
	q.append([x - 1, y - 1, i + 1, 0])

def is_out(x, y):
	if x < 0 or x >= n or y < 0 or y >= n:
		return True
	return False

def is_union():
	for i in range(2, k + 1):
		if parent[1] != parent[i]:
			return False
	return True

def find(i):
	if parent[i] == i:
		return i
	parent[i] = find(parent[i])
	return parent[i]

def union(i, j):
	root_i = find(i)
	root_j = find(j)
	if root_i != root_j:
		parent[root_j] = root_i


while q and not is_union():
    # 현재 연도의 큐 사이즈만큼만 반복하여 동시 전파 구현
    for _ in range(len(q)):
        now_x, now_y, now_num, d_val = q.popleft()
        for d in directions:
            next_x = now_x + d[0]
            next_y = now_y + d[1]
            if is_out(next_x, next_y):
                continue
            if board[next_y][next_x] == 0:
                board[next_y][next_x] = now_num
                q.append([next_x, next_y, now_num, d_val + 1])
            elif board[next_y][next_x] != now_num:
                union(board[next_y][next_x], now_num)
    year += 1

print(year)
