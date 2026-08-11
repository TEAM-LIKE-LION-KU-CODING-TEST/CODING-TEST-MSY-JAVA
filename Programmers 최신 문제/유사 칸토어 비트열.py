def count_ones(n, k):
    # 0번째 단계이거나 k가 0이면 1의 개수는 k
    if n == 0:
        return 1 if k > 0 else 0
    if k == 0:
        return 0
    
    unit_length = 5 ** (n - 1)
    unit_ones = 4 ** (n - 1)
    
    idx = k // unit_length
    rest = k % unit_length
    
    if idx < 2:
        return idx * unit_ones + count_ones(n - 1, rest)
    elif idx == 2:
        return 2 * unit_ones
    else:
        return (idx - 1) * unit_ones + count_ones(n - 1, rest)

def solution(n, l, r):
    return count_ones(n, r) - count_ones(n, l - 1)