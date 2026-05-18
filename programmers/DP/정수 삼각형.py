def solution(triangle):
    answer = 0
    height = len(triangle)
    dp = [[] for _ in range(height)]
    
    dp[0].append(triangle[0][0])
    for i in range(1, height):
        # 해당 높이의 dp 초기화
        dp[i] = [0 for _ in range(i + 1)]
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
                continue
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                continue
            # 이전 높이에서 좌/우에서 오는 경우 중 최댓값
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    
    answer = max(dp[height - 1])   
    return answer