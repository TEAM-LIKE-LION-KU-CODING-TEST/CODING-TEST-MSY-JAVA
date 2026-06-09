#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16928                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16928                          #+#        #+#      #+#     #
#    Solved: 2025/08/21 13:14:28 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys
read = sys.stdin.readline
write = sys.stdout.write

def bfs(ladder, snake):
    ans_len = [0 for _ in range(101)]
    visited = [False for _ in range(101)]

    queue =  deque()
    queue.append(1)
    while queue:
        now = queue.popleft()
        if now == 100:
            return ans_len[100]
        
        # 1~6 주사위 굴리기
        for i in range(1, 7):
            next = now + i
            
            # 해당 칸에 도착했을떄 사다리거나 뱀이면 무조건 타고가야 함
            if next in ladder:
                    next = ladder[next]
            if next in snake:
                    next = snake[next]
            
            if next <= 100 and not visited[next]:
                visited[next] = True
                ans_len[next] = ans_len[now] + 1
                queue.append(next)

# BFS
def main():
    N, M = map(int, read().rstrip().rsplit())
    ladder = {}
    snake = {}
    for _ in range(N):
        x, y = map(int, read().rstrip().rsplit())
        ladder[x] = y
    for _ in range(M):
        u, v = map(int, read().rstrip().rsplit())
        snake[u] = v
    
    answer = bfs(ladder, snake)
    write(f"{answer}")

if __name__ == "__main__":
    main()