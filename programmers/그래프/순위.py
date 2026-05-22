from collections import deque

def bfs(n, graph, count):
    for i in range(1, n + 1):
        # deque 초기화와 함께 첫 노드 입력
        q = deque([i])
        check = [0 for _ in range(n + 1)]
        # 큐에 들어갈 때 체크
        check[i] = 1
        while q:
            now = q.popleft()
            for next in graph[now]:
                if check[next] == 1:
                    continue
                # 큐에 넣을때 체크
                check[next] = 1
                # 해당 노드를 방문할 때 누적
                count[next] += 1
                q.append(next)

def solution(n, results):
    answer = 0
    # 승리/패배 그래프 구성
    win_graph = [[] for _ in range(n + 1)]
    lose_graph = [[] for _ in range(n + 1)]
    count = [0 for _ in range(n + 1)]
    for r in results:
        # 승리 방향으로 그래프 구성
        win_graph[r[0]].append(r[1])
        # 패배 방향으로 그래프 구성
        lose_graph[r[1]].append(r[0])
    
    bfs(n, win_graph, count)
    bfs(n, lose_graph, count)
    
    print(count)
    
    for i in range(1, n + 1):
        if count[i] == n - 1:
            answer += 1
    
    return answer