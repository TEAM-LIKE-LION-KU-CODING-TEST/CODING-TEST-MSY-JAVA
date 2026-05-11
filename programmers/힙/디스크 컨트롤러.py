import heapq

def solution(jobs):
    answer = 0
    
    pq = []
    # 무조건 첫번째 작업은 우선순위 상 최우선으로 보장하여 정렬
    jobs = sorted(jobs, key=lambda x : (x[0], x[1]))
    
    idx = 1
    time = jobs[0][0]
    heapq.heappush(pq, (jobs[0][1], jobs[0][0], 0))
    while pq:
        now = heapq.heappop(pq)
        # 소요 시간만큼 현재 시간에 더하기
        time += now[0]
        # 종료 시간을 jobs 배열에 기록
        jobs[now[2]].append(time)
        
        # 중간에 시간이 뜰 경우 임의로 다음 작업까지 시간 조정
        # pq가 비어있을 경우에만 다음 작업까지 시간 조정
        if idx < len(jobs) and jobs[idx][0] > time and not pq:
            time = jobs[idx][0]
        # 작업이 완료된 후 시간까지 도착한 작업들 큐에 입력
        while idx < len(jobs) and jobs[idx][0] <= time:
            heapq.heappush(pq, (jobs[idx][1], jobs[idx][0], idx))
            idx += 1
    
    for j in jobs:
        answer += j[2] - j[0]
    return answer // len(jobs)