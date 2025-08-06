#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2512                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2512                           #+#        #+#      #+#     #
#    Solved: 2025/07/15 10:59:43 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
write = sys.stdout.write

# 주어진 상한액을 기준으로 예산 배정시의 총 예산 계산
def calculate_total_budget(reqs, lim):
    tot_sum = 0
    for req in reqs:
        # 요청금액이 주어진 상한액보다 작을 경우
        if req <= lim:
            tot_sum += req
        # 요청금액이 주어진 상한액보다 클 경우
        else:
            tot_sum += lim
    return tot_sum

def main():
    N = int(sys.stdin.readline().rstrip())
    reqs = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())

    # 모든 요청 금액의 합이 총 예산보다 작거나 같을 경우
    if sum(reqs) <= M:
        write(str(max(reqs)))
        return
    
    low = 1
    # 이진탐색의 초기 상한은 reqs 값들 중 max
    high = max(reqs)
    answer = 0
    # 이진탐색을 위해 요청 금액 배열 정렬
    reqs.sort()
    while low <= high:
        mid = (low + high) // 2
        # mid를 상한액으로 필요한 총 에산 계산
        cur_budget_sum = calculate_total_budget(reqs, mid)

        # 현재 상한액으로 배정 가능 or 예산 남음
        if cur_budget_sum <= M:
            answer = mid
            low = mid + 1
        # 현재 상한액으로 예산 초과
        else:
            high = mid - 1
    
    write(str(answer))    

if __name__ == "__main__":
    main()