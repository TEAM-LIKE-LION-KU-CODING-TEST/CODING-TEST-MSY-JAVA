def solution(k, room_number):
    answer = []
    # 딕셔너리 (실제 배정된 방만 동적으로 저장)
    parent = {}

    def find(i):
        # 최고 조상 찾기
        an = i
        # parent에 an이 존재한다는 것은 이미 배정된 방이라는 의미
        while an in parent:
            an = parent[an]
            
        # 경로 압축
        cur = i
        while cur != an:
            nxt = parent[cur]
            parent[cur] = an
            cur = nxt
            
        return an

    for rn in room_number:
        # 방이 비어있다면 (딕셔너리에 없다면) 바로 배정
        if rn not in parent:
            answer.append(rn)
            # 다음 빈 방의 가능성이 있는 rn + 1을 부모로 가리키도록 설정
            parent[rn] = rn + 1
        # 방이 이미 찼다면 find 함수로 빈 방 탐색
        else:
            an = find(rn)
            answer.append(an)
            # 새로 찾은 빈 방도 배정되었으므로 an + 1을 가리키도록 설정
            parent[an] = an + 1
            
    return answer
