#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17484                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17484                          #+#        #+#      #+#     #
#    Solved: 2025/07/18 12:55:38 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def main():
    N, M = map(int, read().rstrip().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, read().rstrip().split())))

    # dp[i][j][k]는 (i, j) 위치에 도달했을 때의 최소 연료 소비량
    # k는 이전 경로의 방향
    # 0: 왼쪽 아래 대각선 / 1: 위 / 2: 오른쪽 아래 대각선
    # 무한대로 초기화
    dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

    # 첫 번째 행에서는 어떤 방향에서 오든 동일한 연료 소비량을 가짐
    for j in range(M):
        dp[0][j][0] = board[0][j]
        dp[0][j][1] = board[0][j]
        dp[0][j][2] = board[0][j]
    
    for i in range(1, N):
        for j in range(M):
            # 1. 왼쪽 아래 대각선으로 이동하는 경우
            # 현재 위치 (i, j)가 왼쪽 끝이 아니어야 (j > 0) 이전 열에서 올 수 있음
            if j + 1 < M:
                dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + board[i][j]

            # 2. 바로 아래로 이동하는 경우
            # 현재 위치 (i, j)로 오기 위해서는 (i-1, j)에서 바로 아래로 이동해야 함.
            dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + board[i][j]

            # 3. 오른쪽 아래 대각선으로 이동하는 경우
            # 현재 위치 (i, j)가 오른쪽 끝이 아니어야 (j < M - 1) 이전 열에서 올 수 있음
            if j - 1 >= 0:
                dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + board[i][j]

    min_fuel = float('inf')
    for j in range(M):
        # 세 가지 방향 모두 고려
        for k in range(3):
            min_fuel = min(min_fuel, dp[N - 1][j][k])
            
    write(str(min_fuel))

if __name__ == "__main__":
    main()