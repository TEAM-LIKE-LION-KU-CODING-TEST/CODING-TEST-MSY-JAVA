#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2075                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2075                           #+#        #+#      #+#     #
#    Solved: 2025/08/02 16:11:40 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import heapq
import sys
read = sys.stdin.readline
write = sys.stdout.write

def main():
    N = int(read().rstrip())
    pq = []

    for _ in range(N):
        nums = list(map(int, read().rstrip().rsplit()))
        for num in nums:
            if len(pq) < N:
                heapq.heappush(pq, num)
            # 우선순위 큐의 크기가 N이면, 현재 큐의 최솟값과 비교 후 추가
            else: 
                # 새로운 숫자가 힙의 최솟값보다 크다면
                if num > pq[0]: 
                    # 가장 작은 값 제거
                    heapq.heappop(pq)
                    # 새로운 값 추가
                    heapq.heappush(pq, num)

    write(f"{heapq.heappop(pq)} \n")

if __name__ == "__main__":
    main()