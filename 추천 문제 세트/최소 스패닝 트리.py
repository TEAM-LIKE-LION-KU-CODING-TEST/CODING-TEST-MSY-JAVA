import heapq

T = int(input())
for tc in range(T):
    answer = 0
    V, E = map(int, input().split())
    parent = [i for i in range(V + 1)]
    edge= []
    for _ in range(E):
        A, B, C = map(int, input().split())
        heapq.heappush(edge, (C, A, B))

    def find(i):
        if parent[i] == i:
            return parent[i]
        parent[i] = find(parent[i])
        return parent[i]

    def union(a, b):
        r_a = find(a)
        r_b = find(b)
        if r_a != r_b:
            parent[r_a] = r_b

    cnt = 0
    while cnt < (V - 1):
        cost, a, b = heapq.heappop(edge)

        if find(a) == find(b):
            continue
        # 순환이 생기지 않는다면 현재시점 최소 cost 간선 추가
        union(a, b)
        answer += cost
        cnt += 1

    print(f"#{tc + 1} {answer}")
        
