# 슬라이딩 윈도우
n, d = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

idx = 0
win_size = 1
while idx + win_size < n:
	# 개미 집합에 포함 가능하면 win_size 늘리기
	if p[idx + win_size] - p[idx] <= d:
		win_size += 1
		continue
	# 개미 집합에 포함이 불가하면 idx 이동
	idx += 1
print(n - win_size)