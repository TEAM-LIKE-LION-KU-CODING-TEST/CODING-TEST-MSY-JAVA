def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    
    # 근무 태도 점수 내림차순 동료 평가 점수 오름차순 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    max_peer = 0
    filtered_scores = []
    
    # 인센티브 대상자 선별
    for a, b in scores:
        if b < max_peer:
            if [a, b] == wanho:
                return -1
            continue
        
        max_peer = max(max_peer, b)
        filtered_scores.append(a + b)
        
    # 합계 점수가 높은 순으로 석차 계산
    filtered_scores.sort(reverse=True)
    
    rank = 1
    for s in filtered_scores:
        if s > wanho_sum:
            rank += 1
        else:
            break
            
    return rank