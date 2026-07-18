# 그리디
import sys
import copy

def solution(beginning, target):
    global answer
    answer = sys.maxsize
    # [:]나 .copy()는 모두 shallow copy
    # copy.deepcopy(target)로 deepcopy 수행해야함
    reversed_target = copy.deepcopy(target)
    width = len(beginning[0])
    height = len(beginning)
    
    def swap(a):
        if a == 0:
            return 1
        return 0
    
    # 뒤집힌 target 미리 구하기
    for i in range(height):
        for j in range(width):
            reversed_target[i][j] = swap(reversed_target[i][j])
    
    # is_row에 맞게 실제 배열의 행을 뒤집기
    def reverse(tmp, idx):
        for i in range(width):
            tmp[idx][i] = swap(tmp[idx][i])
    
    # 행의 상태가 고정되면,
    # 각 열을 뒤집을지 말지는 경우의 수가 아니라 강제적으로 결정
    def calculate(row_reverse):
        result = 0
        tmp = copy.deepcopy(beginning)
        
        # 행의 상태 경우의 수에 따라 고정
        for i, r in enumerate(row_reverse):
            if r == 1:
                reverse(tmp, i)
                result += 1
        
        for i in range(width):
            # 모든 칸이 target과 일치하는지 검사
            flag = True
            for j in range(height):
                if tmp[j][i] != target[j][i]:
                    flag = False
            if flag:
                continue
            # 모든 칸이 reversed_target과 일치하는지 검사
            flag = True
            for j in range(height):
                if tmp[j][i] != reversed_target[j][i]:
                    flag = False
            if flag:
                result += 1
                continue
            # 만약 해당 열을 반전으로 만들 수 없다면 바로 return
            # 해당 case는 폐기
            return sys.maxsize
        return result
            
    # 행에 대해서 모든 경우의 수 구하기
    def row_cases(row_reverse, col_now):
        global answer
        
        if col_now >= height:
            answer = min(answer, calculate(row_reverse))
            return
        
        for i in range(2):
            row_reverse[col_now] = i
            row_cases(row_reverse, col_now + 1)
    
    row_cases([0 for _ in range(height)], 0)
    
    if answer == sys.maxsize:
        answer = -1
    return answer