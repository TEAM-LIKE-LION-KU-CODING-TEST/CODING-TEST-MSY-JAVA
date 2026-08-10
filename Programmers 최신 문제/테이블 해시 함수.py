def solution(data, col, row_begin, row_end):
    answer = 0
    data_sorted = sorted(data, key=lambda x : (x[col - 1], -x[0]))
    
    def s_mod(row):
        result = 0
        for d in data_sorted[row - 1]:
            result += d % row
        return result
    
    answer = s_mod(row_begin)
    for i in range(row_begin + 1, row_end + 1):
        # XOR 연산은 ^
        answer ^= s_mod(i)
    return answer