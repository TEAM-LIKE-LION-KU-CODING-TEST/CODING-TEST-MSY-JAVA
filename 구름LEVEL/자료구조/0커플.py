# 투 포인터
answer = 0
n = int(input())
score = list(map(int, input().split()))
score.sort()

left = 0
right = n - 1
while left <= right:
	# 0커플 성사
	if score[left] + score[right] == 0:
		left += 1
		right -= 1
		continue
	# 0커플 성사 불가
	if abs(score[left]) < abs(score[right]):
		answer += score[right]
		right -= 1
	else:
		answer += score[left]
		left += 1
print(answer)