import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N + 2)]
rocks = list(map(int, input().split()))

dp[1:4] = rocks[0:3].copy()
for i in range(4, N + 1):
	dp[i] = min(dp[i - 3], dp[i - 2], dp[i - 1]) + rocks[i - 1]
print(min(dp[N - 2], dp[N - 1], dp[N]))