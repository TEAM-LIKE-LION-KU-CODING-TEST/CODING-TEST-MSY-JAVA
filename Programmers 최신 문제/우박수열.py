def solution(k, ranges):
    answer = []
    conjecture = []
    integration = []
    while k > 1:
        conjecture.append(k)
        if k % 2 == 0:
            k = int(k / 2)
        else:
            k = k * 3 + 1
    conjecture.append(k)
    for i in range(len(conjecture) - 1):
        integration.append((conjecture[i] + conjecture[i + 1]) / 2)
    
    c_len = len(conjecture) - 1
    for st,ed in ranges:
        tmp = 0
        ed = c_len + ed
        if st > ed:
            answer.append(-1)
            continue
        for i in range(st, ed):
            tmp += integration[i]
        answer.append(tmp)
    
    return answer