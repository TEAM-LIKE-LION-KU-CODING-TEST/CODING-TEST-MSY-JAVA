from itertools import combinations

def solution(relation):
    answer = 0
    row_num = len(relation)
    attr_num = len(relation[0])
    # unique_comb에는 이미 검증된 유일성과 최소성을 만족하는 케이스의 list
    unique_comb = [] 
    
    def is_unique(case):
        uni_set = set([])
        for i in range(row_num):
            li = []
            for c in case:
                li.append(relation[i][c])
            # list를 tuple로 변환하여 해시 가능하게 만든다
            tuple_li = tuple(li)
            if tuple_li in uni_set: 
                return False 
            uni_set.add(tuple_li)
        return True

    for i in range(1, attr_num + 1):
        for case in combinations(range(attr_num), i):
            set_case = set(case)
            # 최소성 검사: 이미 찾은 유일키 u 중 하나라도 현재 set_case의 부분집합인지 확인
            if any(u.issubset(set_case) for u in unique_comb):
                continue

            # 유일성 검사: 최소성을 통과한 경우에만 유일성 검사
            if is_unique(case):
                unique_comb.append(set_case)

    answer = len(unique_comb)    
    return answer