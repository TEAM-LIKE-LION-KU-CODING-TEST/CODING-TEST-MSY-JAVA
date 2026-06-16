n = int(input())
MOD = 100000007

def is_valid(x):
	if x & (x << 1):
		return False
	return True

dp = [[0 for _ in range(8)] for _ in range(n)]

for x in range(8):
	if is_valid(x):
		dp[0][x] = 1

for y in range(1, n):
	for x in range(8):
		if not is_valid(x):
			continue
		for prevX in range(8):
			if not is_valid(prevX):
				continue
			if x & prevX:
				continue
			dp[y][x] += dp[y - 1][prevX]
			dp[y][x] %= MOD

print(sum(dp[n - 1]) % MOD)