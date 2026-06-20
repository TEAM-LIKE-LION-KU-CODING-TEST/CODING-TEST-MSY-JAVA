coin_sum = 0
h1, w1 = map(int, input().split())
coin1 = []
for i in range(h1):
	coin1.append(input())
	coin_sum += coin1[i].count("O")

h2, w2 = map(int, input().split())
coin2 = []
for i in range(h2):
	coin2.append(input())

def is_out(y, x):
	if y < 0 or y >= h1 or x < 0 or x >= w1:
		return True
	return False

def process(y_cal, x_cal):
    coin_cnt = 0
    for i in range(h2):
        for j in range(w2):
            if coin2[i][j] == 'O':
                nowY = i - y_cal
                nowX = j - x_cal
                if is_out(nowY, nowX):
                    continue
                # 이동한 위치의 coin1 격자에도 동전이 있다면 카운트 증가
                if coin1[nowY][nowX] == 'O':
                    coin_cnt += 1
    return coin_cnt

max_cnt = 0
# coin2가 coin1의 모서리에 1칸만 걸치는 경우까지 포함하도록 탐색 범위 수정
for i in range(-h1 + 1, h2):
    for j in range(-w1 + 1, w2):
        current_cnt = process(i, j)
        if current_cnt > max_cnt:
            max_cnt = current_cnt
print(coin_sum - max_cnt)