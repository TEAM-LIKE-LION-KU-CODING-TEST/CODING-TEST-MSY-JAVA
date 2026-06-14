n, m = map(int, input().split())
height = list(map(int, input().split()))
# 각 집이 마지막으로 비가 온 날
last_rained = [-3] * n

for day in range(1, m + 1):
	s, e = map(int, input().split())
	# 비 내리기
	for i in range(s-1, e):
		height[i] += 1
		# 마지막 비내린 날 갱신
		last_rained[i] = day
	# 배수 시스템
	if day % 3 == 0:
		for i in range(n):
			# 3일마다 배수 시스템이 작동하므로
			# 마지막으로 갱신된 비내린 날이 2일 이내일 때 조건
			if day - last_rained[i] <= 2:
				height[i] -= 1

for h in height:
	print(h, end=' ')