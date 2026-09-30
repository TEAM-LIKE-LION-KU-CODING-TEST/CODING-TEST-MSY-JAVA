def solution(s):
    answer = 0
    
    def is_right(ns):
        stack = []
        
        for now in ns:
            if now == '[' or now == '(' or now == '{':
                stack.append(now)
                continue
            elif not stack:
                return False
            elif (now == ']' and stack[-1] == '[') or (now == ')' and stack[-1] == '(') or (now == '}' and stack[-1] == '{'):
                stack.pop()
                continue
            return False
        if stack:
            return False
        return True
    
    for i in range(len(s)):
        now_s = s[i:] + s[:i]
        if is_right(now_s):
            answer += 1
        # print(now_s, is_right(now_s))
    
    return answer