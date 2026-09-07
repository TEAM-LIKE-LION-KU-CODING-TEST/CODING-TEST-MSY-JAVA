import sys
sys.setrecursionlimit(10000)

def solution(picks, minerals):
    answer = 0
    # dia : 0, iron : 1, stone : 2
    fatique = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    numerate = {"diamond" : 0, "iron" : 1, "stone" : 2}
    
    def calc(p, idx):
        cnt = 0
        ran = min(5, len(minerals) - idx)
        for i in range(idx, idx + ran):
            cnt += fatique[p][numerate[minerals[i]]]
        return (idx + ran), cnt
    
    def dfs(pick, idx, cnt_sum):
        if idx >= len(minerals) or sum(pick) == 0:
            return cnt_sum

        min_fatigue = sys.maxsize
        for i, p in enumerate(pick):
            if p > 0:
                now_idx, cnt = calc(i, idx)
                pick[i] -= 1
                min_fatigue = min(min_fatigue, dfs(pick, now_idx, cnt_sum + cnt))
                pick[i] += 1
        
        return min_fatigue
    
    answer = dfs(picks, 0, 0)
    return answer