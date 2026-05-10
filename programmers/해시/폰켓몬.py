def solution(nums):
    answer = 0
    
    N = len(nums)
    nums_set = set(nums)
    if len(nums_set) > (N//2):
        answer = N//2
    else:
        answer = len(nums_set)
    
    return answer