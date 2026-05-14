from functools import cmp_to_key

# x+y와 y+x를 비교하여 내림차순 정렬
def compare(x, y):
    if x + y > y + x:
        return -1  # x가 앞에 옴
    elif x + y < y + x:
        return 1   # y가 앞에 옴
    else:
        return 0

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    
    numbers.sort(key=cmp_to_key(compare))
        
    # 결과 합치기 및 '000' 처리
    answer = str(int(''.join(numbers)))
    return answer