#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11501                          #+#        #+#      #+#     #
#    Solved: 2025/07/29 13:46:51 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def main():
    T = int(read().rstrip())
    for _ in range(T):
        N = int(read().rstrip())
        prices = list(map(int, read().rstrip().rsplit()))

        # 역순으로 순회하는 그리디 방식
        answer = 0
        max_price = 0
        for i in range(N - 1, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            else:
                answer += max_price - prices[i]
        write(f"{answer}\n")

if __name__ == "__main__":
    main()