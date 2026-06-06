def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    st = []
    # 별도 시간 변수 대신 enumerate 사용
    for i, p in enumerate(prices):
        # head는 st[-1]로 접근
        # 리스트 자체의 Truthy/Falsy 활용
        while st and p < st[-1][0]:
            now = st.pop()
            answer[now[1]] = i - now[1]
        st.append([p, i])
    
    while st:
        now = st.pop()
        answer[now[1]] = len(prices) - 1 - now[1]
    
    return answer