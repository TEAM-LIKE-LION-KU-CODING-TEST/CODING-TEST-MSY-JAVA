def solution(weights):
    answer = 0
    
    # nC2 조합식 구현
    def combination(n):
        return (n * (n - 1)) // 2
    
    same_nums = {}
    seesaw = {}
    for w in weights:
        same_nums[w] = same_nums.get(w, 0) + 1
        for i in range(2, 5):
            now = i * w
            if now not in seesaw:
                seesaw[now] = {}
            seesaw[now][w] = seesaw[now].get(w, 0) + 1
    
    for k in same_nums.keys():
        if same_nums[k] >= 2:
            answer += combination(same_nums[k])
    
    for k in seesaw.keys():
        length = len(seesaw[k])
        if length >= 2:
            sum_num = 0
            for l in seesaw[k].keys():
                sum_num += seesaw[k][l]
                if seesaw[k][l] >= 2:
                    answer -= combination(seesaw[k][l])
            answer += combination(sum_num)
    
    return answer