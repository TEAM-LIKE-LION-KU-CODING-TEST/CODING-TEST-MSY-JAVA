#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14940                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14940                          #+#        #+#      #+#     #
#    Solved: 2025/08/06 13:05:57 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# BFS
def main():
    mov_pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    n, m = map(int, read().rstrip().rsplit())
    mp = [[0 for _ in range(m)] for _ in range(n)]
    ans = [[0 for _ in range(m)] for _ in range(n)]

    st_coor = []
    for i in range(n):
        rows = list(map(int, read().rstrip().rsplit()))
        for j in range(len(rows)):
            mp[i][j] = rows[j]
            if rows[j] == 2:
                st_coor = [i, j]
    
    queue = [st_coor]
    ans[st_coor[0]][st_coor[1]] = 0
    while queue:
        # queue.pop()은 맨 뒷 요소를 빼기 때문에
        # pop(0)으로 명시적으로 맨 앞 요소를 빼줘야 함
        cur_coor = queue.pop(0)
        for i in range(4):
            next_y = cur_coor[0] + mov_pos[i][0]
            next_x = cur_coor[1] + mov_pos[i][1]
            if next_y >= n or next_y < 0 or next_x >= m or next_x < 0:
                continue
            elif mp[next_y][next_x] == 0 or mp[next_y][next_x] == 2:
                continue
            ans[next_y][next_x] = ans[cur_coor[0]][cur_coor[1]] + 1
            mp[next_y][next_x] = 0
            queue.append([next_y, next_x])

    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if ans[i][j] == 0 and mp[i][j] == 1:
                write("-1 ")
                continue
            write(f"{ans[i][j]} ")
        write("\n")

if __name__ == "__main__":
    main()