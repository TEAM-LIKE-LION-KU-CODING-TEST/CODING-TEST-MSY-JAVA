from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
q = deque([])
dist = [-1 for _ in range(N + 1)]
check = [False for _ in range(N + 1)]
bridge = [[] for _ in range(N + 1)]
for _ in range(M):
	s, e = map(int, input().split())
	bridge[s].append(e)

def bfs():
	if len(bridge[K]) == 0:
		print(-1)
		return
	
	q.append([K, 0])
	check[K] = True
	while q:
		now, cnt = q.popleft()
		cnt += 1
		for next in bridge[now]:
			if check[next]:
				continue
			q.append([next, cnt])
			dist[next] = cnt + abs(next - K)
			check[next] = True

	result = 0
	dist_max = max(dist)
	for i in range(1, N + 1):
		if i == K:
			continue
		if dist[i] >= dist_max:
			result = i
	print(result)

bfs()