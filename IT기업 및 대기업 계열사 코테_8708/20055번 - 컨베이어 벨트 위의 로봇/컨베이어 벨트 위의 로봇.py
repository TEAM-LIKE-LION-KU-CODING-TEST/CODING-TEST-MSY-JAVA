#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20055                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20055                          #+#        #+#      #+#     #
#    Solved: 2025/08/20 13:01:54 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# 투포인터
def main():
    N, K = map(int, read().rstrip().rsplit())
    tmp = list(map(int, read().rstrip().rsplit()))
    Ai = []
    for i in tmp:
        Ai.append([i, False])

    time = 0
    zero_cnt = 0
    left = 0
    right = N - 1
    while zero_cnt < K:
        # 1. 벨트가 각 칸 위의 로봇과 함께 한 칸 회전
        Ai[right][1] = False
        left -= 1
        right -= 1
        if left < 0:
            left = (2 * N) - 1
        if right < 0:
            right = (2 * N) - 1
        # 2. 가장 먼저 올라간 로봇부터 벨트 회전하는 방향으로 움직인다
        idx = right
        out_right = right + 1
        if out_right >= 2 * N:
            out_right = 0
        
        for i in range(N):
            if Ai[idx][1] == True:
                next = idx + 1
                if idx == (2 * N) - 1:
                    next = 0

                if next == out_right:
                    Ai[idx][1] = False
                elif Ai[next][0] > 0 and Ai[next][1] == False:
                    Ai[idx][1] = False
                    Ai[next][1] = True
                    Ai[next][0] -= 1
                    if Ai[next][0] == 0:
                        zero_cnt += 1
            idx -= 1
            if idx < 0:
                idx = (2 * N) - 1
        # 3. 올리는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
        if Ai[left][0] > 0:
            Ai[left][0] -= 1
            Ai[left][1] = True
            if Ai[left][0] == 0:
                zero_cnt += 1
        time += 1

    write(f"{time}")

if __name__ == "__main__":
    main()