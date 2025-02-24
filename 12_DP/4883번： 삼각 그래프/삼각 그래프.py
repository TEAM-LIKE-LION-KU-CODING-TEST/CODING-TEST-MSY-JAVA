#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4883                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4883                           #+#        #+#      #+#     #
#    Solved: 2025/02/24 12:29:12 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
MAX = 987654321

def dynamic(graph, N):
    # dp[i][j] : i, j번째 노드로 도달할 때의 최소비용 (현재 map 값 포함)
    dp = [[0] * 3 for _ in range(N + 1)]

    # 0,0으로 도달할 수 있는 경로가 존재하지 않기 때문에 MAX
    # 무조건 (0, 1)에서 시작해야 한다
    dp[0][0] = MAX
    dp[0][1] = graph[0][1]
    dp[0][2] = dp[0][1] + graph[0][2]

    for i in range(1, N):
        # 0번째 열에서는 이전 행의 0번, 1번에서 올 수 있음
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][0]
        # 1번째 열에서는 이전행의 0번, 1번, 2번 그리고 같은 행의 0번에서 올 수 있음
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2],
                               dp[i][0]) + graph[i][1]
        # 2번째 열에서는 이전행의 1번, 2번 그리고 같은 행의 1번에서 올 수 있음
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][2],
                               dp[i][1]) + graph[i][2]
    
    return dp[N - 1][1]


def main():
    input = sys.stdin.read
    # 전체 입력을 한 번에 받아 시간을 줄이기
    data = input().split("\n")

    cnt = 1
    index = 0
    result = []
    
    while index < len(data):
        N = int(data[index])
        if N == 0:
            break
        
        graph = []
        for i in range(1, N + 1):
            graph.append(list(map(int, data[index + i].split())))

        result.append(f"{cnt}. {dynamic(graph, N)}")
        cnt += 1
        # 입력 개수만큼 인덱스를 증가시킴
        index += N + 1

    # 한번에 result 배열을 전체 출력해 시간 줄이기
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()