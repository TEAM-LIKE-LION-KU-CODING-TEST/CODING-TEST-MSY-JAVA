import heapq

def solution(operations):    
    # 각 숫자에 고유한 ID 값을 부여하여 삭제 여부 추적
    id_idx = 0
    deleted_id = []
    max_heap = []
    min_heap = []
    for op in operations:
        op_str, num = op.split(" ")
        num = int(num)
        if op_str == "I":
            heapq.heappush(max_heap, (-num, id_idx))
            heapq.heappush(min_heap, (num, id_idx))
            deleted_id.append(False)
            id_idx += 1
        else:
            if num == 1:
                # 삭제된 ID라면 계속 꺼냄
                while max_heap and deleted_id[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    val, idx = heapq.heappop(max_heap)
                    deleted_id[idx] = True
            elif num == -1:
                # 삭제된 ID라면 계속 꺼냄
                while min_heap and deleted_id[min_heap[0][1]]: 
                    heapq.heappop(min_heap)
                if min_heap:
                    val, idx = heapq.heappop(min_heap)
                    deleted_id[idx] = True
    
    while max_heap and deleted_id[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while max_heap and deleted_id[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if not max_heap or not min_heap:
        return [0, 0]
    return [-max_heap[0][0], min_heap[0][0]]