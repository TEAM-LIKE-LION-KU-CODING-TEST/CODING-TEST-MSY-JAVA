#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9461                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9461                           #+#        #+#      #+#     #
#    Solved: 2025/03/03 12:42:17 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
print = sys.stdout.write

def main():
    T = int(input().rstrip())
    for i in range(T):
        dp = [0, 1, 1, 1, 2, 2]
        N = int(input().rstrip())

        if(N <= 5):
            print(f"{dp[N]}\n")
            continue
        
        # N > 5일 경우 무조건 연장되는데
        # P(j) = P(j - 1) + P(j - 1 - 4)
        for j in range(6, N + 1):
            dp.append(dp[j - 1] + dp[j - 5])
        
        print(f"{dp[N]}\n")

if __name__ == "__main__" :
    main()