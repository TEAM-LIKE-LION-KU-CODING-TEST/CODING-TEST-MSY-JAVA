from itertools import combinations

def solution(orders, course):
    answer = []
    course.sort()
    
    max_order_len = -1
    for o in orders:
        max_order_len = max(max_order_len, len(o))
    
    def find_course(c_num):
        # 조합별 등장 횟수를 저장할 딕셔너리
        comb_cnt = {}
        # 최대 26 종류의 메뉴의 모든 조합을 검사하는 것이 아닌
        # 최대 길이 10인 order내에서 나올 수 있는 모든 c_num 길이 조합을 카운트
        for order in orders:
            for case in combinations(sorted(list(order)), c_num):
                # 조합을 튜플이나 문자열 키로 카운트
                comb_cnt[case] = comb_cnt.get(case, 0) + 1
        
        cnt_list = {}
        for case, cnt in comb_cnt.items():
            if cnt not in cnt_list:
                cnt_list[cnt] = []
            cnt_list[cnt].append(case)
            
        return cnt_list
    
    for c in course:
        if c > max_order_len:
            break
        course_cnt = find_course(c)
        max_cnt = max(course_cnt.keys())
        if max_cnt < 2:
            continue
        for cc in course_cnt[max_cnt]:
            answer.append("".join(cc))
    answer.sort()
    return answer