from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 총 경과한 시간
    time = 1
    # 다리에 올라가길 대기하는 트럭의 idx
    idx = 0
    # 트럭의 총 개수
    n = len(truck_weights)
    # 현재 다리 위 트럭 무게의 합
    cur_weight = 0
    # 다리 위에 있는 트럭
    q = deque([])
    while idx < n:
        # 일단 무게가 허용하는 만큼 다리에 다 올리기
        while idx < n and (cur_weight + truck_weights[idx]) <= weight:
            q.append([truck_weights[idx], time])
            cur_weight += truck_weights[idx]
            time += 1
            idx += 1
        print(q)
        # 건넌 트럭이 하나라도 있는지 확인하는 flag
        flag = False
        # 다리에 올라가며 지난 시간동안 건넌 트럭이 있는지 검사
        while q and (q[0][1] + bridge_length) <= time:
            flag = True
            now = q.popleft()
            cur_weight -= now[0]
        # 건너간 트럭이 하나라도 있다면 트럭 다시 올리기
        if flag:
            continue
        # 맨 앞의 트럭을 건너게 하기
        now = q.popleft()
        cur_weight -= now[0]
        time += bridge_length - (time - now[1])
    print(q)
    # 전체 루프가 끝난 뒤에도 남은 트럭이 있다면 건너게 하기
    while q:
        now = q.popleft()
        time += bridge_length - (time - now[1])
    
    return time