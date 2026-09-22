from collections import deque

def solution(queue1, queue2):
    answer = -1
    all_len = len(queue1) * 3
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    seq = 0
    while seq < all_len and q1 and q2:
        # print(q1_sum, q2_sum)
        # 항상 합이 더 큰 쪽에서 먼저 빼도록 선택 (그리디)
        if q1_sum > q2_sum:
            now = q1.popleft()
            q1_sum -= now
            q2.append(now)
            q2_sum += now
        elif q1_sum < q2_sum:
            now = q2.popleft()
            q2_sum -= now
            q1.append(now)
            q1_sum += now
        elif q1_sum == q2_sum:
            answer = seq
            break
        seq += 1
    
    return answer