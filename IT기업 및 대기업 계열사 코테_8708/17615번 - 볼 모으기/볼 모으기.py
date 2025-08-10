#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17615                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17615                          #+#        #+#      #+#     #
#    Solved: 2025/08/10 14:09:58 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# 그리디, 하드코딩
def main():
    N = int(read().rstrip())
    balls = read().rstrip()
    red_cnt = balls.count('R')
    blue_cnt = balls.count('B')

    answer = min(red_cnt, blue_cnt)
    seq_cnt = 1
    for i in range(1, N):
        if balls[i] != balls[i - 1]:
            break
        seq_cnt += 1
    
    if balls[0] == 'R':
        answer = min(answer, red_cnt - seq_cnt)
    else:
        answer = min(answer, blue_cnt - seq_cnt)

    seq_cnt = 1
    for i in range(N - 2, -1, -1):
        if balls[i] != balls[i + 1]:
            break
        seq_cnt += 1
    
    if balls[N - 1] == 'R':
        answer = min(answer, red_cnt - seq_cnt)
    else:
        answer = min(answer, blue_cnt - seq_cnt)

    write(str(answer))

if __name__ == "__main__":
    main()