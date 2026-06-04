def solution(tickets):
    answer = []
    ticket_map = {}
    for i in range(len(tickets)):
        if tickets[i][0] not in ticket_map:
            ticket_map[tickets[i][0]] = []
        # 목적지 공항과 tickets 내 인덱스 기록
        ticket_map[tickets[i][0]].append([tickets[i][1], i])
    
    check = [0 for _ in range(len(tickets))]
    def dfs(now, route, cnt):
        # 모든 티켓을 소진했을때
        if cnt == len(tickets):
            # route.copy() 혹은 route[:]으로 복사본 저장
            # route는 리스트 객체의 참조이기 때문
            answer.append(route[:])
            return
        # ticket_map.get(now, [])를 통해 런타임 에러 방지 (티켓이 없을 경우)
        for t in ticket_map.get(now, []):
            if check[t[1]] == 1:
                continue
            # 티켓 사용 내역 기록
            check[t[1]] = 1
            # 경로에 추가
            route.append(t[0])
            dfs(t[0], route, cnt + 1)
            check[t[1]] = 0
            route.pop()
    dfs("ICN", ["ICN"], 0)
    answer.sort()
    return answer[0]