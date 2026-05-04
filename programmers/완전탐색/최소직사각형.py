def solution(sizes):
    answer = 0
    long_side, short_side = [], []
    for w, h in sizes:
        long_side.append(max(w, h))
        short_side.append(min(w, h))
    
    answer = max(long_side) * max(short_side)
    return answer