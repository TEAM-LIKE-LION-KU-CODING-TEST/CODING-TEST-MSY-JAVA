n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = int(input())

for i in range(k):
	for j in range(len(b)):
		b[-1 - j] += 1
		if b[-1 - j] <= a[-1 - j]:
			break
		b[-1 - j] = 0

print("".join(map(str, b)))