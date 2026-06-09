#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2294                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2294                           #+#        #+#      #+#     #
#    Solved: 2025/03/26 15:00:42 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
print = sys.stdout.write
MAX_VAL = 987654321

def main():
    N, K = map(int, input().rstrip().split())

    arr = []
    for i in range(N):
        arr.append(int(input().rstrip()))

    # set은 파이썬의 내장함수로, 중복되지 않은 원소(unique)를 얻고자 할 때 사용 
    # set 자료구조의 특징은 중복이 없다는 점
    arr_set = set(arr)   # set으로 변환
    arr = list(arr_set)  # 리스트로 변환
    # 크기순 정렬
    arr.sort()
    # ⚠️ 중복 제거된 동전 수로 갱신
    N = len(arr)

    dp = []
    for i in range(N):
        dp.append([0])
        for j in range(1, K+1):
            # MAX 값으로 초기화
            dp[i].append(MAX_VAL)

    for i in range(N):
        for j in range(1, K+1):
            if(i - 1 < 0) and (j - arr[i] < 0):
                continue
            elif i - 1 < 0:
                dp[i][j] = dp[i][j - arr[i]] + 1
            elif j - arr[i] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j - arr[i]] + 1)
            
    if(dp[N - 1][K] >= MAX_VAL):
        print("-1")
    else:
        print(str(dp[N - 1][K]))
            
if __name__ == '__main__' :
    main()