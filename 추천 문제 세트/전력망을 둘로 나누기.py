def solution(n, wires):
    answer = float('inf')
    
    def find(i, parent):
        cnt = 0
        root = i
        while root != parent[root]:
            root = parent[root]
            cnt += 1
        
        # 경로 압축
        nxt = i
        while nxt != parent[nxt]:
            prev = nxt
            nxt = parent[nxt]
            parent[prev] = root
        
        return root, cnt
    
    def union(a, b, parent):
        root_a, cnt_a = find(a, parent)
        root_b, cnt_b = find(b, parent)
        if root_a != root_b:
            if cnt_a < cnt_b:
                parent[root_a] = root_b
            else:
                parent[root_b] = root_a
    
    for i in range(len(wires)):
        parent = [i for i in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue
            union(wires[j][0], wires[j][1], parent)
        
        # 마지막 wire까지 union 이후 각 노드에 대해 최종 find
        for i in range(n + 1):
            find(i, parent)
        
        cnt_g1 = 0
        g1 = parent[1]
        for p in parent[1:]:
            if p == g1:
                cnt_g1 += 1
        
        answer = min(answer, abs((n - cnt_g1) - cnt_g1))
    return answer