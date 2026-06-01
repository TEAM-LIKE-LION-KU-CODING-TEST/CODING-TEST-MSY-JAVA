# MST를 찾기 위한 Kruskal + Union Find
def solution(n, costs):
    answer = 0
    edge_cnt = 0
    # 각 node의 부모를 본인으로 설정
    parent = [i for i in range(n)]
    
    def find(idx):
        if parent[idx] == idx:
            return parent[idx]
        # 경로 압축
        parent[idx] = find(parent[idx])
        return parent[idx]

    def union(src, dst):
        root_src = find(src)
        root_dst = find(dst)
        if root_src != root_dst:
            parent[root_dst] = root_src
    
    costs = sorted(costs, key=lambda x : x[2])
    for c in costs:
        src = c[0]
        dst = c[1]
        cost = c[2]
        # cycle 생성 여부 검사
        if find(src) == find(dst):
            continue
        edge_cnt += 1
        answer += cost
        if edge_cnt == (n - 1):
            break
        union(src, dst)
    return answer