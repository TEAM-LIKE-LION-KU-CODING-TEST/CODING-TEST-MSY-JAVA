#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2293                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2293                           #+#        #+#      #+#     #
#    Solved: 2025/03/04 17:16:04 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
print = sys.stdout.write

def main():
    N, K = map(int, input().rstrip().split())

    dp = []
    coin = []
    for i in range(N):
        coin.append(int(input().rstrip()))
    
    # dp[0]번은 1로 초기화
    # 나머지는 0으로 초기화
    dp.append(1)
    for i in range(1, K + 1):
        dp.append(0)

    # 한번에 각 동전에 대한 dp를 구하는 것이 아니라
    # coin[i]번째부터 K번째까지
    # 각 동전에 대해 독립적으로 j를 만드는 조합을 누적
    # 즉, 2차원 배열 형태로 생각하고 이를 누적
    for i in range(N):
        for j in range(coin[i], K + 1):
            dp[j] = dp[j] + dp[j - coin[i]]
    
    print(f"{dp[K]}")


if __name__ == '__main__':
    main()