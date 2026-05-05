def solution(n, lost, reserve):
    answer = 0
    lost_final = sorted(set(lost) - set(reserve))
    reserve_final = sorted(set(reserve) - set(lost))
    
    for r in reserve_final:
        left = r - 1
        right = r + 1
        if left in lost_final:
            lost_final.remove(left)
        elif right in lost_final:
            lost_final.remove(right)
            
    answer = n - len(lost_final)
    return answer