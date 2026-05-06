def solution(N, number):
    s = [set([]) for i in range(9)]
    
    for i in range(1, 9):
        # N, NN, NNN... 추가
        s[i].add(int(str(N) * i))

        # i개를 만들기 위한 조합 j와 i-j
        for j in range(1, i):
            for op1 in s[j]:
                for op2 in s[i-j]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            return i
    
    return -1