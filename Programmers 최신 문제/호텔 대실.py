# 그리디, 방 하나에 최대한 많은 예약을 두는 것이 항상 유리
def solution(book_time):
    answer = 0
    book_time = sorted(book_time, key=lambda x: x[0])
    check = [False for _ in range(len(book_time))]
    
    def is_available(ed, st):
        ed_h, ed_m = map(int, ed.split(":"))
        st_h, st_m = map(int, st.split(":"))
        
        # 청소 시간까지 고려
        ed_m += 10
        if ed_m >= 60:
            ed_h += 1
            ed_m %= 60
        
        if ed_h < st_h:
            return True
        elif ed_h == st_h and ed_m <= st_m:
            return True
        return False
    
    for i in range(len(book_time)):
        if check[i] == True:
            continue
        check[i] = True
        now = i
        answer += 1
        for j in range(i + 1, len(book_time)):
            if check[j]:
                continue
            if is_available(book_time[now][1], book_time[j][0]):
                check[j] = True
                now = j
        if False not in check:
            break
    return answer