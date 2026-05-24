from collections import deque

def solution(s):
    st = deque([])
    
    for i in s:
        if i == '(':
            st.append(i)
            continue
        if len(st) == 0:
            return False
        st.popleft()
    if len(st) != 0:
        return False
    return True