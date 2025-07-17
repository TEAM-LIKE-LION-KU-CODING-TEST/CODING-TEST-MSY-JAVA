#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19941                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19941                          #+#        #+#      #+#     #
#    Solved: 2025/07/17 12:51:24 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
write = sys.stdout.write

def main():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    table = list(sys.stdin.readline().rstrip())
    answer = 0
    for i in range(len(table)):
        if table[i] == 'P':
            left = max(0, i - K)
            right = i + 1
            
            flag = False
            while left != i:
                if table[left] == 'H':
                    table[left] = '_'
                    flag = True 
                    answer += 1
                    break
                left += 1
            # 왼쪽에서 못 찾았을 때
            # 오른쪽으로 증가하는 방향으로 찾아야 최적
            end = min(N, i + K + 1)
            while flag == False and right < end:
                if table[right] == 'H':
                    table[right] = '_' 
                    answer += 1
                    break
                right += 1
    
    write(str(answer))

if __name__ == "__main__":
    main()