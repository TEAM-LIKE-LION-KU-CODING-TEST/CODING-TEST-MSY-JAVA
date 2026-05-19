from collections import deque

def solution(n, computers):
    answer = 0
    
    # 인접행렬을 연결리스트로 생성
    computer_linked = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                computer_linked[i].append(j)
                
    check = [0 for _ in range(n)]
    st_idx = 0
    # sum(check)가 n보다 작을때까지 = 모든 컴퓨터 방문할 때까지
    while sum(check) < n:
        if check[st_idx] == 1:
            st_idx += 1
            continue
        queue = deque([])
        queue.append(st_idx)
        while queue:
            now = queue.popleft()
            check[now] = 1
            for i in computer_linked[now]:
                if check[i] == 1:
                    continue
                queue.append(i)
        # 하나의 BFS 루프가 종료될때마다 네트워크 개수 추가
        answer += 1
    
    return answer