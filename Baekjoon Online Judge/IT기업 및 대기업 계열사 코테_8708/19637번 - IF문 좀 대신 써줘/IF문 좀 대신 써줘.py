#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19637                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19637                          #+#        #+#      #+#     #
#    Solved: 2025/07/24 15:58:26 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
read = sys.stdin.readline
write = sys.stdout.write

def bin_search(powers, power) -> int:
    low = 0
    high = len(powers) - 1
    ans_idx = 0
    while low <= high:
        mid = (low + high) // 2
        # 현재 칭호의 상한값이 캐릭터 전투력보다 크거나 같으면,
        # 해당 칭호가 답이 될 수 있으므로 일단 ans_idx에 저장하고 
        # 더 작은 상한값을 찾기 위해 왼쪽으로 이동
        if powers[mid][1] >= power:
            ans_idx = mid
            high = mid - 1
        # 현재 칭호의 상한값이 캐릭터 전투력보다 작으면,
        # 해당 칭호로는 부족하므로 더 높은 상한값을 찾기 위해 오른쪽으로 이동
        else:
            low = mid + 1
    
    return ans_idx

def main():
    N, M = map(int,read().rstrip().split())
    idx = 0
    powers = []
    for _ in range(N):
        name, power = map(str, read().rstrip().split())
        power = int(power)

        if idx == 0:
            powers.append([name, power])
            idx += 1
            continue

        if powers[idx - 1][1] == power:
            continue

        powers.append([name, power])
        idx += 1

    for _ in range(M):
        power = int(read().rstrip())
        ans_idx = bin_search(powers, power)
        write(powers[ans_idx][0] + "\n")
        
if __name__ == "__main__":
    main()