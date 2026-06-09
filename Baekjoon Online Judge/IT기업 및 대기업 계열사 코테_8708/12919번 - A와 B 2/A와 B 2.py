#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12919                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12919                          #+#        #+#      #+#     #
#    Solved: 2025/08/19 12:12:38 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def recur(S, T):
    if S == T:
        return 1
    elif len(S) > len(T):
        return 0
    
    if T[len(T) - 1] == 'A':
        answer = recur(S, T[0:len(T)-1])
        if answer == 1:
            return 1
    if T[0] == 'B':
        tmp = T[1:]
        answer = recur(S, tmp[::-1])
        if answer == 1:
            return 1
    return 0

def main():
    S = read().rstrip()
    T = read().rstrip()
    answer = recur(S, T)
    write(f"{answer}")

if __name__ == "__main__":
    main()