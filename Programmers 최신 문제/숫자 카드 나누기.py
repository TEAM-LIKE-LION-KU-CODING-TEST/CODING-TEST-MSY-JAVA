import math

def solution(arrayA, arrayB):
    answer = 0
    
    def gcd(arr):
        gcd_val = arr[0]
        for a in arr[1:]:
            gcd_val = math.gcd(gcd_val, a)
        return gcd_val
    
    gcd_a = gcd(arrayA)
    gcd_b = gcd(arrayB)

    # 최대공약수 자체만 검증
    valid_a = True
    for num in arrayB:
        if num % gcd_a == 0:
            valid_a = False
            break
            
    valid_b = True
    for num in arrayA:
        if num % gcd_b == 0:
            valid_b = False
            break
            
    # 조건을 만족하는 경우에만 최대값으로 answer 갱신
    if valid_a:
        answer = max(answer, gcd_a)
    if valid_b:
        answer = max(answer, gcd_b)
        
    return answer