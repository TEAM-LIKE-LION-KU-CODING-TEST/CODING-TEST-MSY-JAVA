T = int(input())
for tc in range(T):
    answer = ""
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]

    def find(i):
        if parent[i] == i:
            return i
        # 경로 압축
        parent[i] = find(parent[i])
        return parent[i]

    # 합집합 연산
    def union(a, b):
        r_a = find(a)
        r_b = find(b)
        if r_a != r_b:
            parent[r_a] = r_b

    for _ in range(m):
        cmd, a, b = map(int, input().split())
        if cmd == 0:
            union(a, b)
        else:
            answer += "1" if find(a) == find(b) else "0"

    print(f"#{tc + 1} {answer}")
