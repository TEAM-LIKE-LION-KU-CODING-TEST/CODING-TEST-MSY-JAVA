from collections import deque

def solution(enroll, referral, seller, amount):
    answer = {e : 0 for e in enroll}
    referral_dict = {}
    for i, e in enumerate(enroll):
        referral_dict[e] = referral[i]
    # level은 1부터 시작, "-"는 center
    level = {"-": 1}
    for i in range(len(enroll)):
        level[enroll[i]] = level[referral[i]] + 1
    max_level = max(level.values())
    enroll_level = [[] for _ in range(max_level + 1)]
    for k in level.keys():
        enroll_level[level[k]].append(k)
    
    enroll_q = {"-": deque([])}
    for e in enroll:
        enroll_q[e] = deque([])
        
    for i, s in enumerate(seller):
        enroll_q[s].append(amount[i] * 100)
    
    for i in range(max_level, 1, -1):
        for now in enroll_level[i]:
            # print(now, enroll_q[now])
            while enroll_q[now]:
                profit = enroll_q[now].popleft()
                profit_10 = (profit * 10) // 100
                if profit_10 <= 0:
                    answer[now] += profit
                    continue
                answer[now] += profit - profit_10
                enroll_q[referral_dict[now]].append((profit * 10) // 100)
    
    return list(answer.values())