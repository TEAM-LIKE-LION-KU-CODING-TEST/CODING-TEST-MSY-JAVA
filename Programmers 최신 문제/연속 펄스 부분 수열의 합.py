import sys
from collections import deque

# 카데인 알고리즘 : 누적 합 차이를 이용한 구간 최대 합 구하기
def solution(sequence):
    answer = -1 * sys.maxsize
    
    for s in [1, -1]:
        now = s
        prefix = [0 for _ in range(len(sequence))]
        prefix[0] = sequence[0] * now
        for i in range(1, len(sequence)):
            now *= -1
            prefix[i] = prefix[i - 1] + (sequence[i] * now)
        
        # 최대 구간합 찾기
        idx = -1
        max_prefix = -1 * sys.maxsize
        for i, p in enumerate(prefix):
            # 같은 구간합이면 뒤에 있는게 더 유리
            if p >= max_prefix:
                idx = i
                max_prefix = p
        
        if max_prefix >= 0:
            # 최대 구간합이 양수일 경우
            # 이전 구간합에서 최소인 음수 찾기
            min_prefix = 0
            for i in range(idx - 1, -1, -1):
                min_prefix = min(min_prefix, prefix[i])
            # 최대 구간합에서 그 범위 내 최소 구간합 빼주기 (실제 펄스 수열에서 제외)
            max_prefix -= min_prefix
        answer = max(answer, max_prefix)
    
    return answer