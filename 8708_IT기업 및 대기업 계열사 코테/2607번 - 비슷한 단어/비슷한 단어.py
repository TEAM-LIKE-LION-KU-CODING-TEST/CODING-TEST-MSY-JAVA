#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2607                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2607                           #+#        #+#      #+#     #
#    Solved: 2025/07/21 12:30:07 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# Type Hinting 문법
# char는 함수의 매개변수 이름
# str은 char가 string 타입이어야 한다는 것을 나타냄
# -> int는 이 함수의 반환값을 의미
def alpha_to_num(char: str) -> int:
    # ord() : 입력된 char의 유니코드 값을 가져옴
    return ord(char) - ord('A')

# Python은 Call by Reference
def count_word(word, word_cnt):
    for char in word:
        word_cnt[alpha_to_num(char)] += 1

def count_difference(src_cnt, dst_cnt):
    # 다른 단어의 개수 카운트
    diff_words = 0
    # 다름 정도를 카운트
    diff_num = 0
    for i in range(26):
        now_diff = abs(src_cnt[i] - dst_cnt[i])
        if now_diff != 0:
            diff_num += now_diff
            diff_words += 1
    
    if diff_num == 0:
        return True
    elif diff_words == 1 and diff_num == 1:
        return True
    elif diff_words == 2 and diff_num == 2:
        return True
    return False

def main():
    N = int(read().rstrip())

    if N == 0:
        write("0")
        return

    first_word_cnt = [0] * 26
    answer = 0

    # 첫 단어의 개수 세기
    first_word = read().rstrip()
    count_word(first_word, first_word_cnt)
    first_word_len = len(first_word)
    # 다음 단어들 비교
    for _ in range(N - 1):
        next_word_cnt = [0] * 26
        next_word = read().rstrip()

        # 두 단어의 길이가 2이상 차이날 경우 불가능
        if abs(first_word_len - len(next_word)) >= 2:
            continue

        count_word(next_word, next_word_cnt)
        if count_difference(first_word_cnt, next_word_cnt) is True:
            answer += 1

    write(str(answer) + "\n")

if __name__ == "__main__":
    main()