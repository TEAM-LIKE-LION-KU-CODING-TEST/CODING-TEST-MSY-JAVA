import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
q = deque([])
lab = []
check = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
	tmp = input()
	if "&" in tmp:
		stY = i
		stX = tmp.index("&")
		# [y, x, cnt]
		q.append([stY, stX, 0])
		check[stY][stX] = 1
	lab.append(tmp)

def is_out(y, x):
	if y < 0 or y >= R or x < 0 or x >= C:
		return True
	return False

flag = False
while q and not flag:
	y, x, c = q.popleft()
	for d in directions:
		nY = y + d[0]
		nX = x + d[1]
		if is_out(nY, nX):
			continue
		if lab[nY][nX] == "@":
			print(c)
			flag = True
			break
		if lab[nY][nX] != "#" and check[nY][nX] == 0:
			q.append([nY, nX, c + 1])
			check[nY][nX] = 1
if not flag:
	print(-1)