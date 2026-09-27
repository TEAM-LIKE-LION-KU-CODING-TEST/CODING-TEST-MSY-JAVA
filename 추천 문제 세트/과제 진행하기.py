def solution(plans):
    p_len = len(plans)
    answer = []
    # String 형태 시간 정규화 및 형변환
    for i in range(p_len):
        h, m = map(int, plans[i][1].split(":"))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    plans = sorted(plans, key=lambda x : x[1])
    # print(plans)
    
    q = []
    cur = 0
    cur_time = plans[cur][1]
    while cur < p_len - 1:
        # 현재 작업 시간 이후 다음 작업이 존재할 경우
        if cur_time + plans[cur][2] > plans[cur + 1][1]:
            q.append(cur)
            plans[cur][2] -= (plans[cur + 1][1] - plans[cur][1])
            cur_time += (plans[cur + 1][1] - plans[cur][1])
            cur += 1
        # 현재 작업 시간 이후 다음 작업이 존재하지 않을 경우
        else:
            answer.append(plans[cur][0])
            cur_time += plans[cur][2]
            
            while q:
                q_now = q.pop()
                if cur_time + plans[q_now][2] > plans[cur + 1][1]:
                    plans[q_now][2] -= (plans[cur + 1][1] - cur_time)
                    q.append(q_now)
                    break
                answer.append(plans[q_now][0])
                cur_time += plans[q_now][2]
            
            # 만약 큐도 비었고 다음 작업까지 시간이 뜨는 경우
            # 임의로 다음 작업 시작 시간에 맞춘다
            if cur_time < plans[cur + 1][1]:
                cur_time = plans[cur + 1][1]
            cur += 1
    
    # print(cur_time, plans[cur], q)
    while q:
        if cur_time + plans[q[-1]][2] > plans[cur][1]:
            break
        answer.append(plans[q[-1]][0])
        cur_time += plans[q[-1]][2]
        q.pop()
    answer.append(plans[cur][0])
    while q:
        q_now = q.pop()
        answer.append(plans[q_now][0])
    
    return answer