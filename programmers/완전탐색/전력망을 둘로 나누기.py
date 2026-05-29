from collections import deque
import sys

def topology_count(start, check, map):
    cnt = 0
    q = deque([])
    q.append(start)
    check[start] = 1
    while q:
        now = q.popleft()
        for i in map[now]:
            if check[i] == 1:
                continue
            q.append(i)
            check[i] = 1
            cnt += 1
    return cnt

def solution(n, wires):
    answer = sys.maxsize
    for i in range(len(wires)):
        check = [0 for _ in range(n + 1)]
        map = [[] for _ in range(n + 1)]
        # 무방향 그래프
        for j in range(len(wires)):
            if i == j:
                continue
            map[wires[j][0]].append(wires[j][1])
            map[wires[j][1]].append(wires[j][0])
        topology_1 = topology_count(1, check, map)
        topology_2 = 0
        for i in range(2, n + 1):
            if check[i] == 0:
                topology_2 = topology_count(i, check, map)
                break
        answer = min(answer, abs(topology_1 - topology_2))
    return answer