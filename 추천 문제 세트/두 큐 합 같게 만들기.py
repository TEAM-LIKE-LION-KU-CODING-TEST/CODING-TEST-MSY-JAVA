from collections import deque

def solution(queue1, queue2):
    answer = -1
    cnt = 0
    q_len = len(queue1)
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    while cnt < q_len * 3:
        if sum_1 == sum_2:
            answer = cnt
            break
        
        if sum_1 > sum_2:
            now = q1.popleft()
            sum_1 -= now
            q2.append(now)
            sum_2 += now
        elif sum_1 < sum_2:
            now = q2.popleft()
            sum_2 -= now
            q1.append(now)
            sum_1 += now
        cnt += 1
    
    return answer