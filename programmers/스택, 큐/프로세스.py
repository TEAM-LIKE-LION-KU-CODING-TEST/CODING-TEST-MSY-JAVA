import heapq

def solution(priorities, location):
    n = len(priorities)
    
    max_heap = []
    for p in priorities:
        heapq.heappush(max_heap, -p)
    
    now = 0
    cnt = 1
    check = [0 for _ in range(n)]
    while cnt <= n:
        if priorities[now] >= (max_heap[0] * -1) and check[now] == 0:
            heapq.heappop(max_heap)
            check[now] = cnt
            cnt += 1
        now += 1
        now %= n
    return check[location]