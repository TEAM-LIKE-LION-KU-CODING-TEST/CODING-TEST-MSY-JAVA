def solution(citations):
    answer = 0
    citations = sorted(citations, key=lambda x : -x)
    for i, c in enumerate(citations):
        if c < i + 1:
            return i
    # 모든 논문이 인용 횟수 조건을 만족하는 경우
    return len(citations)