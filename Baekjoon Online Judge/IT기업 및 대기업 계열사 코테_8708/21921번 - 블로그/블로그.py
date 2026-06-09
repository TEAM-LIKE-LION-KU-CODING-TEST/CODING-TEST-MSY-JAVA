#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 21921                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/21921                          #+#        #+#      #+#     #
#    Solved: 2025/07/16 12:04:39 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
write = sys.stdout.write

def main():
    N, X = map(int, sys.stdin.readline().rstrip().split())
    visits = list(map(int, sys.stdin.readline().rstrip().split()))
    
    max = 0
    max_cnt = 1
    for i in range(X):
        max += visits[i]

    left = 0
    cur_sum = max
    for i in range(X, N):
        cur_sum -= visits[left]
        left += 1
        cur_sum += visits[i]

        if cur_sum > max:
            max = cur_sum
            max_cnt = 1
        elif cur_sum == max:
            max_cnt += 1
    
    if max == 0:
        write("SAD")
        return
    write(f"{max}\n{max_cnt}")


if __name__ == "__main__":
    main()