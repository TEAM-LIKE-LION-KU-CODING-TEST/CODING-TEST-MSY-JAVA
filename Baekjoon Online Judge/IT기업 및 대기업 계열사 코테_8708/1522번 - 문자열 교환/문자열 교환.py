#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1522                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1522                           #+#        #+#      #+#     #
#    Solved: 2025/08/13 13:23:48 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# 투 포인터 - 슬라이딩 윈도우
def main():
    string = read().rstrip()
    a_len = string.count('a')

    # 원형 문자열 처리
    string += string[0:a_len - 1]
    min_val = float('inf')
    for i in range(len(string) - (a_len - 1)):
        # 슬라이딩 윈도우 내의 b의 개수가 현재 윈도우의 교환횟수가 됨
        min_val = min(min_val, string[i:i+a_len].count('b'))
    write(str(min_val))

if __name__ == "__main__":
    main()