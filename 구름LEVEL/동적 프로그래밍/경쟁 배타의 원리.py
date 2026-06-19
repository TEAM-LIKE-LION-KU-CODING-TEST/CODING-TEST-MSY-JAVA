# 2차원 차분 배열(imos), 2차원 누적 합
n, k = map(int, input().split())
diff_arr = [[0 for _ in range(1002)] for _ in range(1002)]
for i in range(n):
	x1, y1, x2, y2 = map(int, input().split())
	diff_arr[x1][y1] += 1
	diff_arr[x2][y2] += 1
	diff_arr[x1][y2] += -1
	diff_arr[x2][y1] += -1

# 가로 누적 합 후 세로 누적 합
for i in range(1001):
	for j in range(1001):
		diff_arr[i][j] = diff_arr[i][j] + diff_arr[i][j - 1]

for i in range(1001):
	for j in range(1001):
		diff_arr[i][j] = diff_arr[i][j] + diff_arr[i - 1][j]

answer = 0
for i in range(1001):
	for j in range(1001):
		if diff_arr[i][j] == k:
			answer += 1
print(answer)