from collections import deque

def solution(x, y, n):
    answer = 0
    dp = [-1 for _ in range(y + 1)]
    
    dp[x] = 0
    for i in range(x, y + 1):
        calc = []
        prevs = [i - n, i // 2 if i % 2 == 0 else 0, i // 3 if i % 3 == 0 else 0]
        for p in prevs:
            if p <= 0:
                continue
            if dp[p] == -1:
                continue
            calc.append(p)
        if len(calc) == 0:
            continue
        dp[i] = dp[calc[0]] + 1 if dp[i] == -1 else dp[i]
        for j in range(1, len(calc)):
            dp[i] = min(dp[i], dp[calc[j]] + 1)
    
    answer = dp[y]
    return answer