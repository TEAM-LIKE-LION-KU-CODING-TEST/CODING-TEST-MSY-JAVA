#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15989                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15989                          #+#        #+#      #+#     #
#    Solved: 2025/08/16 13:18:05 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# DP
# 점화식을 세워, 1만 사용하는 경우, 2를 포함하는 경우,
# 3을 포함하는 경우의 수를 각각 계산한 후 모두 더하여 답을 찾음
def main():
    T = int(read().rstrip())
    for _ in range(T):
        n = int(read().rstrip())
        # n이 특수한 경우의 예외처리
        if n == 1:
            write("1\n")
            continue
        elif n == 2:
            write("2\n")
            continue
        elif n == 3:
            write("3\n")
            continue

        # 1로 n까지의 숫자를 만드는 경우는 항상 1가지이므로
        dp = [[1 for _ in range(n + 1)]]
        dp.append([0 for _ in range(n + 1)])
        dp.append([0 for _ in range(n + 1)])
        dp[1][2] = 1
        for i in range(3, n + 1):
            dp[1][i] = dp[0][i - 2] + dp[1][i - 2]

        dp[2][3] = 1
        for i in range(4, n + 1):
            dp[2][i] = dp[0][i - 3] + dp[1][i - 3] + dp[2][i - 3]
                
        answer = dp[0][n] + dp[1][n] + dp[2][n]
        write(f"{answer}\n")
        
if __name__ == "__main__":
    main()