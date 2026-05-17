def is_prime(num):
    if (num == 0) or (num == 1):
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def dfs(depth, numbers, current, limit, check, nums):
    if depth == limit:
        nums.add(int(''.join(current)))
        return
    
    for i in range(len(numbers)):
        if check[i] == 1:
            continue
            
        check[i] = 1
        current.append(numbers[i])
        
        dfs(depth + 1, numbers, current, limit, check, nums)
        
        current.pop()
        check[i] = 0
    
def solution(numbers):
    answer = 0
    nums = set([])
    
    for i in range(1, len(numbers) + 1):
        check = [0 for _ in range(len(numbers))]
        dfs(0, numbers, [], i, check, nums)
    
    for n in nums:
        if is_prime(n):
            answer += 1
    
    return answer