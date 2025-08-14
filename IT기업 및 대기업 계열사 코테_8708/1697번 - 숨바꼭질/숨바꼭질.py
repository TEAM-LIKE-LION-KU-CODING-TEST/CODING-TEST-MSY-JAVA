#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1697                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1697                           #+#        #+#      #+#     #
#    Solved: 2025/08/14 16:40:23 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

MAX = 100000

def bfs(N, K, dist):
    q = []
    q.append(N)
    while q:
        x = q.pop(0)
        # 만약 현재 위치가 동생의 위치 K라면
        if x == K:
            return dist[x]

        # 이동이 가능한 모든 위치값을 dir로 하여 BFS
        dir = [x - 1, x + 1, x * 2]
        for i in dir:
            if 0<= i <= MAX and not dist[i]:
                dist[i] = dist[x] +1
                q.append(i)
# BFS
def main():
    N, K = map(int, read().rstrip().rsplit())
    # 동생의 위치 K를 넘어서서도 이동이 가능하므로
    dist = [0 for _ in range(MAX + 1)]
    answer = bfs(N, K, dist)
    write(f"{answer}")

if __name__ == "__main__":
    main()