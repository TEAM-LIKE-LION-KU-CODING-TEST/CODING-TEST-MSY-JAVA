def solution(today, terms, privacies):
    answer = []
    # 모든 달은 28일까지 있다고 가정
    type = {}
    
    def norm(date):
        year, month, day = date.split(".")
        return ((int(year) * 12) + int(month)) * 28 + int(day)
    
    today_norm = norm(today)
    for t in terms:
        name, month = t.split(" ")
        type[name] = int(month) * 28
    
    # print(type)
    for i, p in enumerate(privacies):
        date, t = p.split(" ")
        # print(date, t, norm(date), today_norm)
        if today_norm - norm(date) >= type[t]:
            answer.append(i + 1)
    
    return sorted(answer)