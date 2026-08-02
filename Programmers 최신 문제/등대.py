import sys
# 파이썬의 최대 재귀 깊이를 늘려 런타임 오류 방지
sys.setrecursionlimit(200000)

def solution(n, lighthouse):
    answer = 0
    is_on = [False for _ in range(n + 1)]
    route = {i : [] for i in range(1, n + 1)}
    for light in lighthouse:
        route[light[0]].append(light[1])
        route[light[1]].append(light[0])
    
    def dfs(now, prev):
        for next in route[now]:
            if next == prev:
                continue
            # 자식 등대의 불이 꺼져있다면
            # 나의 불은 항상 켜져야 한다
            if not dfs(next, now):
                is_on[now] = True
        return is_on[now]
    
    dfs(1, 0)
    
    for on in is_on:
        if on:
            answer += 1
    
    return answer