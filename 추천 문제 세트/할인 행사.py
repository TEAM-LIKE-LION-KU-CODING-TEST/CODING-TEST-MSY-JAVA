def solution(want, number, discount):
    answer = 0
    w_len = len(want)
    d_len = len(discount)
    cur_sale = {}
    
    for i in range(10):
        cur_sale[discount[i]] = cur_sale.get(discount[i], 0) + 1
        
    def can_buy():
        for i in range(w_len):
            cur_num = cur_sale.get(want[i], -1)
            if number[i] > cur_num:
                return False
        return True
    
    left = 0
    right = 9
    while True:
        # print(cur_sale)
        if can_buy():
            answer += 1

        if right + 1 >= d_len:
            break
        
        cur_sale[discount[left]] -= 1
        cur_sale[discount[right + 1]] = cur_sale.get(discount[right + 1], 0) + 1
        left += 1
        right += 1
        
    return answer