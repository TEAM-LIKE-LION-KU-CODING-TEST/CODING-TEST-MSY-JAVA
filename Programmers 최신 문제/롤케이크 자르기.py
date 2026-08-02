def solution(topping):
    answer = 0
    s1 = {}
    s2 = {}
    
    s1[topping[0]] = s1.get(topping[0], 0) + 1
    for i in range(1, len(topping)):
        s2[topping[i]] = s2.get(topping[i], 0) + 1
    
    for i in range(1, len(topping) - 1):
        if len(s1) == len(s2):
            answer += 1
        s1[topping[i]] = s1.get(topping[i], 0) + 1
        s2[topping[i]] = s2.get(topping[i], 0) - 1
        if s2[topping[i]] <= 0:
            del s2[topping[i]]
    
    return answer