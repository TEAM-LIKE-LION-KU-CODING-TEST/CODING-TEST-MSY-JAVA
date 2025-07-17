#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2193                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2193                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 21:56:21 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
output = sys.stdout.write

def main():
    N = int(input().rstrip())
    # 1, 2자리 이친수는 무조건 1개만 존재
    if(N == 1 or N == 2):
        print("1")
    else:
        # 이후부터는 피보나치 수열
        a = 1; b = 1
        for _ in range(3, N + 1):
            c = a + b
            a = b
            b = c
        print(b)

if __name__ == "__main__":
    main()