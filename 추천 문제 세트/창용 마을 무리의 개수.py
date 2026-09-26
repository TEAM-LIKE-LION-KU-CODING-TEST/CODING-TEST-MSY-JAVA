T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    # 1번부터 N번까지 사람 번호가 붙어있음
    parent = [i for i in range(N + 1)]

    def find(i):
        # 자신이 부모인 노드, 최상위 부모를 찾았다면 종료
        if parent[i] == i:
            return i
        # 경로 압축
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        # 두 부모가 다를 경우 합치기
        if root_i != root_j:
            parent[root_j] = root_i

    for i in range(M):
        a, b = map(int, input().split())
        union(a, b)
        # print(a, b, parent)

    # 남은 union 관계 정리
    for i in range(1, N + 1):
        parent[i] = find(i)

    # print(parent, end='\n\n')
    print(f"#{tc + 1} {len(set(parent)) - 1}")
