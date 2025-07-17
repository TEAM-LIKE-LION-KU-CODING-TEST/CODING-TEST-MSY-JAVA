#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10844                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10844                          #+#        #+#      #+#     #
#    Solved: 2025/02/22 21:33:46 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
MOD = 1_000_000_000

def count_stair_numbers(N):
    # DP 테이블 초기화 (dp[i][j] : 길이가 i이고, 마지막 숫자가 j인 계단 수의 개수)
    dp = [[0] * 10 for _ in range(N + 1)]

    # 길이가 1일 때, 1~9는 모두 계단 수 (0은 포함되지 않음)
    for j in range(1, 10):
        dp[1][j] = 1

    # DP 점화식 적용
    for i in range(2, N + 1):
        for j in range(10):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]  # j-1에서 올라오는 경우
            if j < 9:
                dp[i][j] += dp[i - 1][j + 1]  # j+1에서 내려오는 경우
            dp[i][j] %= MOD  # 문제에서 요구한 나머지 연산 적용

    # 길이가 N인 계단 수의 총합을 구함
    return sum(dp[N]) % MOD

# 입력 처리
N = int(input().strip())
print(count_stair_numbers(N))