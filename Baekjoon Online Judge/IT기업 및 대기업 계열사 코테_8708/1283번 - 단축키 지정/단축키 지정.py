#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1283                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1283                           #+#        #+#      #+#     #
#    Solved: 2025/08/15 14:04:57 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# HashMap
def main():
    N = int(read().rstrip())
    options = []
    hint_idx = [-1 for _ in range(N)]
    hint_dict = {}
    for i in range(N):
        option = read().rstrip()
        options.append(option)
        # 대소문자 구분하지 않기 위해
        option = option.lower()
        saved = False

        # 1. 각 단어의 첫글자 단축키 지정 여부
        idx = 0
        words = option.rsplit(' ')
        for word in words:
            key = word[0]
            if key not in hint_dict:
                hint_idx[i] = idx
                hint_dict[key] = True
                saved = True
                break
            idx += len(word) + 1
        if saved:
            continue

        # 2. 왼쪽부터 차례로 보면서 단축키 지정
        for j in range(len(option)):
            if option[j] == ' ':
                continue
            if option[j] not in hint_dict:
                hint_idx[i] = j
                hint_dict[option[j]] = True
                break

    for i in range(N):
        if hint_idx[i] == -1:
            write(f"{options[i]}\n")
            continue
        for j in range(len(options[i])):
            if j == hint_idx[i]:
                write(f"[{options[i][j]}]")
                continue
            write(f"{options[i][j]}")
        write("\n")

if __name__ == "__main__":
    main()