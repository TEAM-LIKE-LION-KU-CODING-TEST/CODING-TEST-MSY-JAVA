from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    while q:
        tail = len(q) - 1
        # 현재 하나만 남아있으면 무조건 구출하고 종료
        if tail == 0:
            answer += 1
            break
        # 최솟값 + 최댓값이 limit보다 작으면
        elif (q[0] + q[tail]) <= limit:
            q.popleft()
            q.pop()
            answer += 1
            continue
        q.pop()
        answer += 1
    return answer