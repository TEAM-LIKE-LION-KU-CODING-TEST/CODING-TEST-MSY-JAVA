from collections import deque

def solution(arr):
    answer = []
    q = deque([])
    q.append(arr[0])
    
    for i in range(1, len(arr)):
        if q[-1] == arr[i]:
            continue
        q.append(arr[i])
        
    while q:
        answer.append(q.popleft())
    
    return answer