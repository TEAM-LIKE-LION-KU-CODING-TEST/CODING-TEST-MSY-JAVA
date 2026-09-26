import heapq

def solution(n, s, a, b, fares):
    answer = float('inf')
    # graph[src] = [dst, cost]
    graph = [[] for _ in range(n + 1)]
    
    for f in fares:
        graph[f[0]].append([f[1], f[2]])
        graph[f[1]].append([f[0], f[2]])
    
    def dijkstra(start):
        distance = [float('inf') for _ in range(n + 1)]
        
        q = []
        # [현재까지의 최단거리, 현재 노드]
        heapq.heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            
            # 이미 처리된 경로는 continue
            if distance[now] < dist:
                continue
                
            for g in graph[now]:
                next_dist = dist + g[1]
                if next_dist < distance[g[0]]:
                    distance[g[0]] = next_dist
                    heapq.heappush(q, (next_dist, g[0]))
        return distance
        
    st_dist = dijkstra(s)
    a_dist = dijkstra(a)
    b_dist = dijkstra(b)
    
    for i in range(1, n + 1):
        answer = min(answer, st_dist[i] + a_dist[i] + b_dist[i])
    return answer