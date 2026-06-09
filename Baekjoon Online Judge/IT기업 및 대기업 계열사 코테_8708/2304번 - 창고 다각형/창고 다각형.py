#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2304                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2304                           #+#        #+#      #+#     #
#    Solved: 2025/07/30 11:33:55 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def main():
    N = int(read().rstrip())
    pillars = []
    max_h = 0
    max_l = 0
    
    for _ in range(N):
        l, h = map(int, read().rstrip().split())
        pillars.append((l, h))
        if h > max_h:
            max_h = h
            max_l = l

    pillars.sort()
    
    answer = 0
    current_max_height = 0
    for i in range(len(pillars)):
        l, h = pillars[i]
        if h > current_max_height:
            current_max_height = h
        if l == max_l:
            break
        width = pillars[i+1][0] - l
        answer += width * current_max_height

    current_max_height = 0
    for i in range(len(pillars) - 1, -1, -1):
        l, h = pillars[i]
        if h > current_max_height:
            current_max_height = h
        if l == max_l:
            break
        width = l - pillars[i-1][0]
        answer += width * current_max_height

    answer += max_h
    write(str(answer))

if __name__ == "__main__":
    main()