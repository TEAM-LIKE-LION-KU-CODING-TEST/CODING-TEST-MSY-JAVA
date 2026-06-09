#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 22233                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/22233                          #+#        #+#      #+#     #
#    Solved: 2025/07/25 13:04:40 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def main():
    N, M = map(int, read().rstrip().rsplit())
    # dictionary인 keywords 생성
    keywords = {}
    for _ in range(N):
        key = str(read().rstrip())
        keywords[key] = True
    
    for _ in range(M):
        inputs = list(read().rstrip().rsplit(","))
        for i in inputs:
            if i not in keywords:
                continue
            del keywords[i]
        write(str(len(keywords)) + "\n")
    
if __name__ == "__main__":
    main()