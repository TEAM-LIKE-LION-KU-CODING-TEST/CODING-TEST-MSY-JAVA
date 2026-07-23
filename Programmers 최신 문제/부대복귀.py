from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    dist = [-1 for _ in range(n + 1)]
    route = {i : [] for i in range(1, n + 1)}
    for st, ed in roads:
        route[st].append(ed)
        route[ed].append(st)
    
    q = deque([])
    dist[destination] = 0
    q.append([destination, 0])
    while q:
        now, cur_dist = q.popleft()
        for next in route[now]:
            if dist[next] != -1:
                continue
            dist[next] = cur_dist + 1
            q.append([next, cur_dist + 1])
            
    for s in sources:
        answer.append(dist[s])
    return answer