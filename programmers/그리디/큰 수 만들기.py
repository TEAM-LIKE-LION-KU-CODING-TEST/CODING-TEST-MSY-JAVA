def solution(number, k):
    stack = []
    
    # 스택에 값이 있고, 제거할 k가 남았으며, 스택의 마지막 값이 현재 값보다 작을 때 반복 제거
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        
        stack.append(num)
    
    # 순회가 끝났는데도 k가 남은 경우
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)