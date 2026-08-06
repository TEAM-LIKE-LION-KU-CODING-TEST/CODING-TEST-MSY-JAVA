import sys
MAX_SIZE = sys.maxsize

def solution(numbers):
    answer = 0
    
    # 각 번호판을 좌표값으로 변환
    num_pos = []
    num_pos.append([3, 1])
    for i in range(3):
        for j in range(3):
            num_pos.append([i, j])
    # 두 번호 사이의 위치를 구하는 함수
    def dist(a, b):
        result = 0
        x = abs(a[0] - b[0])
        y = abs(a[1] - b[1])
        if x == 0 and y == 0:
            return 1
        while x != 0 or y != 0:
            if x >= 1 and y >= 1:
                x -= 1
                y -= 1
                result += 3
                continue
            elif x >= 1:
                x -= 1
            elif y >= 1:
                y -= 1
            result += 2
        return result
    
    # index, left, right
    dp = [[[MAX_SIZE for _ in range(10)] for _ in range(10)] for _ in range(len(numbers) + 2)]
    dp[0][4][6] = 0
    
    index = 1
    for num in numbers:
        n = int(num)
        for i in range(10):
            for j in range(10):
                # 이전 index에서의 유효한 값 찾기
                if dp[index - 1][i][j] == MAX_SIZE:
                    continue
                # 왼쪽 갱신
                if n != j:
                    dp[index][n][j] = min(dp[index][n][j], dp[index - 1][i][j] + dist(num_pos[i], num_pos[n]))
                # 오른쪽 갱신
                if n != i:
                    dp[index][i][n] = min(dp[index][i][n], dp[index - 1][i][j] + dist(num_pos[j], num_pos[n]))
        index += 1
    
    answer = MAX_SIZE
    for i in dp[index - 1]:
        for j in i:
            if j < answer:
                answer = j
    return answer