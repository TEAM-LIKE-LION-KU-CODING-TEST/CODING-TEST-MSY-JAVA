import sys
input = sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))
# dp[i][x][y] : i번째 요리까지 마쳤고
# 방금 사용한 인덕션을 제외한 나머지 두 인덕션의 온도가
# x, y일 때의 최소 조작 횟수
dp = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(N)]

def get_min_diff(a, b):
    diff = abs(a - b)
    return min(diff, 10 - diff) 

def solution():
    INF = float('inf')
    dp = [[INF for _ in range(10)] for _ in range(10)]
    
    dp[0][0] = 0
    prev = 0
    
    for target in t:
        next_dp = [[INF for _ in range(10)] for _ in range(10)]
        
        for x in range(10):
            for y in range(10):
                if dp[x][y] != INF:
                    # 1. 방금 사용한 인덕션을 다시 사용하는 경우
                    cost_prev = get_min_diff(prev, target)
                    if dp[x][y] + cost_prev < next_dp[x][y]:
                        next_dp[x][y] = dp[x][y] + cost_prev
                        
                    # 2. 온도가 x인 인덕션을 사용하는 경우
                    cost_x = get_min_diff(x, target)
                    if dp[x][y] + cost_x < next_dp[prev][y]:
                        next_dp[prev][y] = dp[x][y] + cost_x
                        
                    # 3. 온도가 y인 인덕션을 사용하는 경우
                    cost_y = get_min_diff(y, target)
                    if dp[x][y] + cost_y < next_dp[prev][x]:
                        next_dp[prev][x] = dp[x][y] + cost_y
                        
        dp = next_dp
        prev = target
        
    min_cost = INF
    for x in range(10):
        for y in range(10):
            if dp[x][y] < min_cost:
                min_cost = dp[x][y]
                
    print(min_cost)

solution()