import sys
sys.setrecursionlimit(200000)

# 시간 복잡도 최악 4**7 * 100 * 7로 완전탐색
def solution(users, emoticons):
    answer = [-1, -1]
    sale_rate = [0 for _ in range(len(emoticons))]

    def calculate():
        e_plus = 0
        e_amount = 0
        for u in users:
            price = 0
            for i, e in enumerate(emoticons):
                if sale_rate[i] >= u[0]:
                    price += e * ((100 - sale_rate[i]) / 100)
                if price >= u[1]:
                    e_plus += 1
                    price = -1
                    break
            if price != -1:
                e_amount += price
        
        if answer[0] < e_plus:
            answer[0] = e_plus
            answer[1] = e_amount
        elif answer[0] == e_plus and answer[1] < e_amount:
            answer[1] = e_amount
    
    def recur(idx):
        if idx == len(emoticons):
            calculate()
            return

        for rate in [10, 20, 30, 40]:
            sale_rate[idx] = rate
            recur(idx + 1)
    
    recur(0)
    return answer