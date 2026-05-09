def solution(n, times):
    answer = 0
    # 시간을 정해두고 역산하기
    # T분이라는 시간이 주어졌을때, 모든 심사관이 최대 몇 명을 심사할 수 있는가?
    left = 1
    # 가장 느린 심사관이 혼자서 모든 사람 처리 시간
    right = max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        total = sum(mid // time for time in times)
        # total == n일때도 조건에 부합
        if total >= n:
            if answer == 0:
                answer = mid
            answer = min(answer, mid)
            right = mid
        else:
            left = mid + 1
    
    return answer