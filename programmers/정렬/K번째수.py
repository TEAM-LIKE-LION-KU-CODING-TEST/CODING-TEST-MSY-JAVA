def solution(array, commands):
    answer = []
    for i, j, k in commands:
        tmp = sorted(array[i - 1:j])
        answer.append(tmp[k - 1])
    
    return answer