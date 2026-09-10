def solution(sequence, k):
    MAX_LEN = 1000010
    
    # [st 인덱스, ed 인덱스, 부분수열 길이]
    answer = [MAX_LEN, MAX_LEN, MAX_LEN]
    cnt = 0
    left = 0
    right = 0
    
    while right < len(sequence):
        if left >= right:
            right = left
            if sequence[right] > k:
                break
        
        if cnt < k and (cnt + sequence[right]) <= k:
            cnt += sequence[right]
            right += 1
            continue
        else:
            if cnt == k:
                length = right - left + 1
                if length < answer[2]:
                    answer = [left, right - 1, length]
            cnt -= sequence[left]
            left += 1
    
    if cnt == k:
        length = right - left + 1
        if length < answer[2]:
            answer = [left, right - 1, length]
    
    return answer[:2]