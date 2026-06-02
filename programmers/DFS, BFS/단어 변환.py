from collections import deque

def solution(begin, target, words):
    # 변환할 수 없는 경우는 즉시 반환
    if target not in words:
        return 0
    
    # 두 글자의 서로 다른 글자가 1개인지 검사
    def is_near(a, b):
        flag = False
        for i in range(len(a)):
            if a[i] != b[i]:
                if flag:
                    return False
                flag = True
        return flag
    
    # 그래프 및 체크 dictionary 생성
    graph = {}
    check = {}
    for w in words:
        check[w] = 0
        graph[w] = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_near(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    
    q = deque([])
    # begin에서 인접한 모든 word 큐 삽입
    for w in words:
        if is_near(begin, w):
            q.append([w, 1])
            check[w] = 1
    # BFS 수행
    while q:
        now = q.popleft()
        if now[0] == target:
            return now[1]
        for w in graph[now[0]]:
            if check[w] == 1:
                continue
            q.append([w, now[1] + 1])