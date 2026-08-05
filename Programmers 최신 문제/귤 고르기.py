def solution(k, tangerine):
    answer = 0
    type = {}
    for t in tangerine:
        type[t] = type.get(t, 0) + 1
    for i in sorted(type.values(), reverse=True):
        k -= i
        answer += 1
        if k <= 0:
            break
    return answer