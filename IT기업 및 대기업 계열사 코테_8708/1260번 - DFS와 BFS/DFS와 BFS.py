#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1260                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1260                           #+#        #+#      #+#     #
#    Solved: 2025/08/05 12:17:01 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def dfs(loc, route, check):
    write(f"{loc} ")
    check[loc] = 1
    for next in route[loc]:
        if check[next] == 1:
            continue
        dfs(next, route, check)
    
    return

def bfs(N, start, route):
    queue = [start]
    check = [0 for _ in range(N + 1)]
    check[start] = 1
    while queue:
        loc = queue.pop(0)
        write(f"{loc} ")
        
        for next in route[loc]:
            if check[next] == 1:
                continue
            queue.append(next)
            check[next] = 1

def main():
    N, M, V = map(int, read().rstrip().rsplit())
    route = {i: [] for i in range(N + 1)}
    for _ in range(M):
        src, dst = map(int, read().rstrip().rsplit())
        route[src].append(dst)
        route[dst].append(src)
    
    # 최소 정점부터 찾아갈 수 있도록 정렬
    for key in route:
        route[key] = sorted(route[key])
    
    dfs(V, route, [0 for _ in range(N + 1)])
    write("\n")
    bfs(N, V, route)

if __name__ == "__main__":
    main()