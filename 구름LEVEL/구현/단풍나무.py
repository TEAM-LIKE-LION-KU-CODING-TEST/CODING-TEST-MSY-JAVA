N = int(input())
answer = 0
flag = True
directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
park = []
park2 = []
for _ in range(N):
	park.append(list(map(int, input().split())))
park2 = [[0 for _ in range(N)] for _ in range(N)]

def is_out(y, x):
	if y < 0 or y >= N or x < 0 or x >= N:
		return True
	return False

def count(y, x):
	cnt = 0
	for d in directions:
		nY = y + d[1]
		nX = x + d[0]
		if is_out(nY, nX):
			continue
		if flag == True and park[nY][nX] == 0:
			cnt += 1
		if flag == False and park2[nY][nX] == 0:
			cnt += 1
	return cnt

def is_end():
	for i in range(N):
		for j in range(N):
			if flag == True and park[i][j] != 0:
				return False
			if flag == False and park2[i][j] != 0:
				return False
	return True

while not is_end():	
	for i in range(N):
		for j in range(N):
			if flag == True:
				park2[i][j] = max(park[i][j] - count(i, j), 0)
			if flag == False:
				park[i][j] = max(park2[i][j] - count(i, j), 0)

	if flag:
		flag = False
	else:
		flag = True
	answer += 1

print(answer)