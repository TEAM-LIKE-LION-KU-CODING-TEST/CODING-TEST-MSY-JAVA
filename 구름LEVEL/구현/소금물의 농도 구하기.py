import math

N, M = map(int, input().split())
salt = N * 0.07
result = salt / (N + M) * 100
print(format(math.floor(result * 100) / 100, ".2f"))