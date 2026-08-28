def solution(numbers):
    answer = []
    n = len(numbers)
    # 배열 초기값을 -1로 설정하여 스택에 남은 인덱스는 -1로 유지
    answer = [-1] * n
    stack = []
    
    for i in range(n):
        # 스택이 비어있지 않고 현재 값이 스택이 가리키는 값보다 크면 뒷 큰수 확정
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer