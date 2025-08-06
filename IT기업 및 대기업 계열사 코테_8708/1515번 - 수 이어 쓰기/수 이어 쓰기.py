#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1515                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1515                           #+#        #+#      #+#     #
#    Solved: 2025/07/16 12:36:04 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
write = sys.stdout.write

def main():
    str_input = sys.stdin.readline().rstrip()
    ptr = 0
    # 1부터 시작하여 숫자를 증가시키면서 확인
    for num in range(1, 30001):
        # 현재 숫자를 문자열로 변환
        num_to_str = str(num)

        # 변환된 숫자의 각 자릿수를 순회
        for char_digit in num_to_str:
            # ptr가 str_input의 길이 미만이고
            # 현재 str_input의 문자가 num_to_str의 현재 자릿수와 일치하는지 확인
            if ptr < len(str_input) and str_input[ptr] == char_digit:
                ptr += 1 # 일치하면 포인터를 증가

            # ptr가 str_input의 길이와 같아지면,
            # str_input 전체가 부분 수열로 발견된 것
            if ptr == len(str_input):
                write(str(num))
                return

if __name__ == "__main__":
    main()