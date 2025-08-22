#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20437                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20437                          #+#        #+#      #+#     #
#    Solved: 2025/08/22 15:17:26 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import Counter
read = sys.stdin.readline
write = sys.stdout.write

def main():
    T = int(read())
    for _ in range(T):
        string = read().strip()
        k = int(read())

        # 문자열 내 각 문자의 빈도수 계산
        counts = Counter(string)
        
        min_len = float('inf')
        max_len = -1

        # 문자열의 모든 문자를 시작점으로 순회
        for i in range(len(string)):
            # 시작 문자의 빈도수가 K보다 작으면 K개의 문자를 포함할 수 없으므로 건너뜀
            if counts[string[i]] < k:
                continue

            # 시작 문자의 등장 횟수 카운트
            count_of_start_char = 0
            for j in range(i, len(string)):
                if string[j] == string[i]:
                    count_of_start_char += 1
                
                # K번 등장했다면, 길이를 계산하고 현재 시작점에 대한 탐색 종료
                if count_of_start_char == k:
                    length = j - i + 1
                    min_len = min(min_len, length)
                    max_len = max(max_len, length)
                    break

        if max_len == -1:
            write("-1\n")
        else:
            write(f"{min_len} {max_len}\n")

if __name__ == "__main__":
    main()