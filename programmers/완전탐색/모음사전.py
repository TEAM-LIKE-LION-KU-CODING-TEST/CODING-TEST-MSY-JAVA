def solution(word):
    answer = 0
    words = []
    alpha = ["A", "E", "I", "O", "U"]
    
    def dfs(now_word, depth, limit):
        if depth == limit:
            words.append("".join(now_word))
            return
        for a in alpha:
            now_word.append(a)
            dfs(now_word, depth + 1, limit)
            now_word.pop()
    
    # 길이 1~5에 따라 만들기
    for i in range(5):
        dfs([], 0, i + 1)
    # 전체 words 사전순 정렬
    words.sort()
    # 완전탐색으로 순서 찾기
    for w in words:
        if w == word:
            break
        answer += 1
    
    return answer + 1