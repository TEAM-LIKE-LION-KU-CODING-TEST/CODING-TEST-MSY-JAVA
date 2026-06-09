#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1138                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1138                           #+#        #+#      #+#     #
#    Solved: 2025/08/04 12:33:39 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# 그리디
def main():
    N = int(read().rstrip())
    orders = list(map(int, read().rstrip().rsplit()))
    answer = [0 for _ in range(N)]

    cur_person = 1
    for order in orders:
        cnt = 0
        for i in range(N):
            if answer[i] == 0:
                if cnt == order:
                    answer[i] = cur_person
                    break
                cnt += 1
        cur_person += 1
    
    for ans in answer:
        write(f"{ans} ")

if __name__ == "__main__":
    main()