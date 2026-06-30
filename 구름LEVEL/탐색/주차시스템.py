from collections import deque

N, M = map(int, input().split())
directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
answer = 0
parking = []
for _ in range(N):
	parking.append(list(map(int, input().split())))

def is_out(y, x):
	if y < 0 or y >= N or x < 0 or x >= M:
		return True
	return False

def bfs(stY, stX):
	result = 0
	if parking[stY][stX] == 0:
			result += 1
	else:
			result -= 2
	
	q = deque([])
	q.append([stY, stX])
	parking[stY][stX] = 1
	while q:
		now = q.popleft()
		for d in directions:
			nY = now[0] + d[0]
			nX = now[1] + d[1]
			if is_out(nY, nX):
				continue
			if parking[nY][nX] == 1:
				continue
			
			if parking[nY][nX] == 0:
				result += 1
			else:
				result -= 2
			q.append([nY, nX])
			parking[nY][nX] = 1
	if result < 0:
		result = 0
	return result
				
for i in range(N):
	for j in range(M):
		if parking[i][j] != 1:
			answer = max(answer, bfs(i, j))

print(answer)