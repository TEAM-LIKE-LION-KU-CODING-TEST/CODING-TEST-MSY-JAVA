#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2531                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2531                           #+#        #+#      #+#     #
#    Solved: 2025/08/11 13:02:14 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

# Queue + Dictionary
def main():
    N, d, k, c = map(int, read().rstrip().rsplit())
    sushi_list = []
    for _ in range(N):
        sushi_list.append(int(read().rstrip()))
    
    answer = 1
    queue = []
    check = {}
    for i in range(N + k):
        # 회전초밥이기 때문에 리스트 끝에서 k 만큼 도는 경우도 고려
        if i >= N:
            i %= N
        sushi = sushi_list[i]
        
        if len(queue) >= k:
            poped = queue.pop(0)
            check[poped] -= 1
            if check[poped] == 0:
                del check[poped]
        
        queue.append(sushi)
        if sushi not in check:
            check[sushi] = 1
        else:
            check[sushi] += 1

        now_answ = len(check) + (c not in check)
        if now_answ > answer:
            answer = now_answ
    
    write(str(answer))

if __name__ == "__main__":
    main()