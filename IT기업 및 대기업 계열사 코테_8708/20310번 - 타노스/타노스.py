#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20310                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20310                          #+#        #+#      #+#     #
#    Solved: 2025/07/23 13:07:05 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def main():
    S = list(read().rstrip())
    zero_num = S.count('0')
    one_num = S.count('1')

    pop_idx = []
    cumulate = 0
    for i in range(len(S)):
        if(S[i] == '1'):
            pop_idx.append(i)
            cumulate += 1

        if cumulate == (one_num / 2):
            break
    
    cumulate = 0
    for i in range(len(S)):
        idx = len(S) - i - 1
        if(S[idx] == '0'):
            pop_idx.append(idx)
            cumulate += 1

        if cumulate == (zero_num / 2):
            break

    pop_pos = 0
    pop_idx.sort()
    for i in range(len(S)):
        if pop_pos < len(pop_idx) and pop_idx[pop_pos] == i:
            pop_pos += 1
            continue
        write(S[i])

if __name__ == "__main__":
    main()