def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    left = 1
    right = distance
    while left <= right:
        # 현재 시점에서 제거한 돌의 개수
        cnt = 0
        # 정답으로 가정한 최소 거리
        mid = (left + right) // 2
        # 기준점
        pivot = 0
        
        # 제거해야 하는 바위 개수 카운트
        for r in rocks:
            dist = r - pivot
            if dist < mid:
                cnt += 1
            else:
                pivot = r
        # 마지막 바위와 도착점 비교
        if (distance - pivot) < mid:
            cnt += 1
        
        if cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
        
        print(left, mid, right)
    
    return answer