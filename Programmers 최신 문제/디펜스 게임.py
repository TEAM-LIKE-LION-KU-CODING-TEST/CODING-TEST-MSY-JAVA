import heapq

def solution(n, k, enemy):
    answer = 0
    
    pq = []
    for e in enemy:
        n -= e
        heapq.heappush(pq, -e)
        if n < 0:
            if k == 0:
                break
            n -= heapq.heappop(pq)
            k -= 1
        answer += 1
    return answer