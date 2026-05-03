import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    while True:
        min_f = heapq.heappop(scoville)
        if min_f >= K:
            return cnt
        if not scoville:
            break
        
        min_s = heapq.heappop(scoville)
        new = min_f + (min_s * 2)
        heapq.heappush(scoville, new)
        cnt+=1
    
    return -1