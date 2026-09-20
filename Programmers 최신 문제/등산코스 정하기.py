import heapq

def solution(n, paths, gates, summits):
    INF = float("inf")
    answer = [INF, INF]
    
    # summits 배열이 정렬되어 있지 않기 때문에 정렬
    summits_set = set(sorted(summits))
    graph = [[] for _ in range(n + 2)]
    for p in paths:
        graph[p[0]].append([p[1], p[2]])
        graph[p[1]].append([p[0], p[2]])
    
    # 다익스트라 변형으로 풀이 가능
    def dijkstra(n):
        # 이때의 distance는 누적 경로가 아닌 현재 경로까지의 최대 단일 weight
        distance = [INF] * (n + 2)
        
        q = []
        for g in gates:
            # heapq는 원소 순서대로 0번부터 순위를 매김
            heapq.heappush(q, (0, g))
            distance[g] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            
            # 현재 노드가 summits (이미 도착했다면) 무시
            if now in summits_set:
                continue
            # 현재 노드가 이미 처리된 적 있는 노드라면 무시
            if distance[now] < dist:
                continue
            
            for g in graph[now]:
                # cost는 현재 경로 내 최댓값과 추가할 경로 중 큰 값
                cost = max(dist, g[1])
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))
        
        return distance
    
    distance = dijkstra(n)
    for i, d in enumerate(distance):
        if i in summits_set and d < answer[1]:
            answer = [i, d]
    
    return answer