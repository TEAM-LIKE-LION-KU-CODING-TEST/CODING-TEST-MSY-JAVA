def recur(k, dungeons, n, check, now, cnt):
    if (k < dungeons[now][0]):
        # 현재 던전 탐험에 실패했으므로 이전까지의 성공 횟수 반환
        return cnt - 1
    # 더 이상 방문할 던전이 없을 경우 현재 횟수가 최대값
    max_val = cnt
    k -= dungeons[now][1]
    for i in range(n):
        if check[i] == 1:
            continue
        check[i] = 1
        max_val = max(max_val, recur(k, dungeons, n, check, i, cnt + 1))
        check[i] = 0
    return max_val

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    # 시작점이 되는 경우는 별도로 입력
    for i in range(n):
        check = [0 for _ in range(n)]
        check[i] = 1
        answer = max(answer, recur(k, dungeons, n, check, i, 1))
    return answer