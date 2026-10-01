def solution(info, query):
    answer = []
    lang = {"-" : 0, "cpp" : 1, "java" : 2, "python" : 3}
    part = {"-" : 0, "backend" : 1, "frontend" : 2}
    exp = {"-" : 0, "junior" : 1, "senior" : 2}
    food = {"-" : 0, "chicken" : 1, "pizza" : 2}
    table = [[[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)]
    all_comb = []
    
    def combination_recur(cur, depth):
        if depth == 4:
            all_comb.append(cur[:])
            return
        for i in range(2):
            cur.append(i)
            combination_recur(cur, depth + 1)
            cur.pop()
    combination_recur([], 0)
    
    for i in info:
        l, p, e, f, score = i.split(" ")
        for ac in all_comb:
            i0 = lang[l if ac[0] == 1 else "-"]
            i1 = part[p if ac[1] == 1 else "-"]
            i2 = exp[e if ac[2] == 1 else "-"]
            i3 = food[f if ac[3] == 1 else "-"]
            table[i0][i1][i2][i3].append(int(score))
    # print(table)
    
    for i in range(4):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    table[i][j][k][l].sort()
    
    def bin_search(left, right, li, target):
        mid = (left + right) // 2
        
        if left > right:
            return mid
        
        if li[mid] >= target:
            return bin_search(left, mid - 1, li, target)
        else:
            return bin_search(mid + 1, right, li, target)
        
    for q in query:
        l, t1, p, t2, e, t3, f, score = q.split()
        now_table = table[lang[l]][part[p]][exp[e]][food[f]]
        if len(now_table) == 0:
            answer.append(0)
            continue
        # print(l, p, e, f, score, now_table)
        loc = bin_search(0, len(now_table) - 1, now_table, int(score))
        # print(loc)
        answer.append(len(now_table) - (loc + 1))
    
    return answer