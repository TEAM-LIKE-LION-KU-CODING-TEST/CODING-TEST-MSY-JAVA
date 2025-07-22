#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3758                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3758                           #+#        #+#      #+#     #
#    Solved: 2025/07/22 12:52:54 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def main():
    T = int(read().rstrip())
    for _ in range(T):
        n, k, t, m = map(int, read().rstrip().split())
        # 팀ID: [문제별 점수 리스트], 제출 횟수, 마지막 제출 시간
        # 문제 번호는 1번부터이므로 k+1의 리스트 크기
        teams = {i: [[0] * (k + 1), 0, 0] for i in range(1, n + 1)}

        # 로그 엔트리는 시간 순서대로 들어옴
        for sub_time in range(m):
            i, j, s = map(int, read().rstrip().split())

            # teams[i][0][j]: 1번째 팀의 문제별 점수 리스트에서 j번째 문제의 점수
            # 동일 문제에 대해서 여러번 제출했을 경우 최댓값이 해당 문제의 점수가 되도록
            if teams[i][0][j] < s:
                teams[i][0][j] = s
            
            teams[i][1] += 1
            teams[i][2] = sub_time
        
        rank_data = []
        for id in range(1, n + 1):
            rank_data.append((id, sum(teams[id][0]), teams[id][1], teams[id][2]))

        # 최종점수에 대해 내림차순
        # 제출 횟수 오름차순
        # 마지막 제출 시간 오름차순
        rank_data.sort(key = lambda x: (-x[1], x[2], x[3]))

        for idx in range(0, n):
            if rank_data[idx][0] == t:
                write(str(idx + 1) + "\n")
                break

if __name__ == "__main__":
    main()