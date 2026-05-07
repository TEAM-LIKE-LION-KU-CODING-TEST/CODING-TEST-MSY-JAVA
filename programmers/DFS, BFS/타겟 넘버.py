answer = 0

def dfs(cur, idx, numbers, target):
    # 전역변수 사용 명시
    global answer
    
    if idx >= len(numbers):
        if cur == target:
            answer += 1
        return
    
    dfs(cur + numbers[idx], idx + 1, numbers, target)
    dfs(cur - numbers[idx], idx + 1, numbers, target)

def solution(numbers, target):
    # 전역변수 사용 명시
    global answer
    dfs(0, 0, numbers, target)
    return answer