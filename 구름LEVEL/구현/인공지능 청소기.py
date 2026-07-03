import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	x, y, N = map(int, input().split())
	cor_sum = abs(x) + abs(y)
	if N < cor_sum:
		print("NO")
		continue
	if (N - cor_sum) % 2 == 1:
		print("NO")
		continue
	print("YES")