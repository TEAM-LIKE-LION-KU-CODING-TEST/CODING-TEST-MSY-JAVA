import heapq

def solution(N, road, K):
    answer = 0

    dist = [float('inf') for _ in range(N + 2)]
    # (dst, cost)
    route = [[] for _ in range(N + 2)]
    
    for r in road:
        route[r[0]].append([r[1], r[2]])
        route[r[1]].append([r[0], r[2]])
    
    def dijkstra():
        q = []
        
        # heapq에는 (지금까지의 비용, 현재 위치)
        heapq.heappush(q, (0, 1))
        dist[1] = 0
        
        while q:
            # 현재 now까지의 전체 비용, 현재 위치
            cost, now = heapq.heappop(q)
            
            # 만약 이미 최솟값이 갱신된 상태라면 continue
            if dist[now] < cost:
                continue
            for r in route[now]:
                # 현재 위치에서 다음 위치까지의 경로 비용
                # cost + r[1] (현재 노드에서 다음 노드까지의 weight)
                next_cost = cost + r[1]
                # 만약 다음 위치까지의 전체 경로 비용이
                # 이미 기록된 dist (최소비용) 보다 작다면 갱신 후 q에 유효한 값으로 삽입
                if next_cost < dist[r[0]]:
                    dist[r[0]] = next_cost
                    heapq.heappush(q, (next_cost, r[0]))
            
    dijkstra()
    
    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1
    
    return answer