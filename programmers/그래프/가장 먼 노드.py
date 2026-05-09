import sys
from collections import deque

def solution(n, edge):
    INF = sys.maxsize
    q = deque([])
    answer = 0
    
    # edge 정보를 그래프 형태로 초기화
    # bidirectional
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    check = [0] * (n + 1)
    dist = [INF] * (n + 1)
    
    # 출발지, 목적지 형태로 큐에 삽입
    q.append((0, 1))
    
    cnt = 0
    dist[0] = 0
    while q:
        now = q.popleft()
        src = now[0]
        dst = now[1]
        dist[dst] = min(dist[dst], dist[src] + 1)
        
        if check[dst] == 1:
            continue
        check[dst] = 1
        for i in graph[dst]:
            q.append((dst, i))
    
    max_val = max(dist)
    for i in dist:
        if i == max_val:
            answer+=1
    
    return answer