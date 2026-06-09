#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1927                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1927                           #+#        #+#      #+#     #
#    Solved: 2025/07/28 15:46:08 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# 기본적으로 최소 힙이며
# 값에 -를 넣어 최대 힙처럼 사용할 수 있다
import heapq
import sys
read = sys.stdin.readline
write = sys.stdout.write

def main():
    pq = []
    N = int(read().rstrip())
    for _ in range(N):
        num = int(read().rstrip())
        if num == 0:
            if len(pq) == 0:
                write("0 \n")
                continue
            write(str(heapq.heappop(pq)) + "\n")
        else:
            heapq.heappush(pq, num)

if __name__ == "__main__":
    main()