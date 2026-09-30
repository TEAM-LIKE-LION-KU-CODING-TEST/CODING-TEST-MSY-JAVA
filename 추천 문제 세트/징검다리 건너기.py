import heapq

def solution(stones, k):
    answer = 0
    
    q = []
    for i in range(k):
        heapq.heappush(q, [-stones[i], i])
    answer = -q[0][0]
    
    for i in range(k, len(stones)):
        # print(q, i, i - k)
        heapq.heappush(q, [-stones[i], i])
        while q[0][1] <= i - k:
            heapq.heappop(q)
        answer = min(answer, -q[0][0])
    
    return answer