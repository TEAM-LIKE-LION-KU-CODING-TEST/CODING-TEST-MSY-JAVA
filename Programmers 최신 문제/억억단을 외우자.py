import heapq

def solution(e, starts):
    answer = []
    min_s = min(starts)
    
    # 미리 최소 s부터 e까지 전체 수들의 등장 빈도 구하기
    # (s=1) ~ (e=5000000) > 최악의 경우 77,896,938
    num_cnt = [0 for _ in range(e - min_s + 1)]
    for i in range(1, e + 1):
        now = i
        weight = 1
        while True:
            if now * weight > e:
                break
            # 음수 인덱싱 주의
            if (now * weight) < min_s:
                weight += 1
                continue
            num_cnt[now * weight - min_s] += 1
            weight += 1
    
    # e부터 최소 s까지 모든 범위에 해당하는 값 미리 구하기
    pq = []
    result_arr = [0 for _ in range(e - min_s + 1)]
    for i in range(e, min_s - 1, -1):
        heapq.heappush(pq, [-num_cnt[i - min_s], i])
        result_arr[i - min_s] = pq[0][1]
    
    # starts의 s에 맞는 순서대로 answer에 갱신
    for s in starts:
        answer.append(result_arr[s - min_s])
    return answer