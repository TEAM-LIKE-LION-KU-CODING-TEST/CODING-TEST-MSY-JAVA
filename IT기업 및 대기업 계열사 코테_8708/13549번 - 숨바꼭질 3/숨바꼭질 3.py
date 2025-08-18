#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13549                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13549                          #+#        #+#      #+#     #
#    Solved: 2025/08/18 12:41:37 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

MAX = 100000
def bfs(N, K, check):
    # 시작 위치는 N이므로
    # BFS를 위한 큐에 N 초기값
    queue = [N]
    check[N] = 0
    while queue:
        loc = queue.pop(0)

        dir = [loc - 1, loc + 1]
        for i in range(2):
            next = dir[i]
            if next < 0 or next > MAX:
                continue
            if check[next] > check[loc] + 1:
                check[next] = check[loc] + 1
                queue.append(next)
        
        next = loc * 2
        if next < 0 or next > MAX:
            continue
        if check[next] > check[loc]:
            check[next] = check[loc]
            queue.append(next)

def main():
    N, K = map(int, read().rstrip().rsplit())
    check = [(MAX + 1) for _ in range(MAX + 1)]
    bfs(N, K, check)
    write(f"{check[K]}")
    
if __name__ == "__main__":
    main()