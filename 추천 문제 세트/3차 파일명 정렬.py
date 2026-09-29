def solution(files):
    answer = []
    div_file = []
    numbers = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    
    for f in files:
        f_len = len(f)
        idx = 0
        HEAD = ""
        
        while f[idx] not in numbers:
            HEAD += f[idx]
            idx += 1
        
        NUMBER = ""
        while idx < f_len and f[idx] in numbers:
            NUMBER += f[idx]
            idx += 1
        
        TAIL = f[idx:]
        div_file.append([HEAD, NUMBER, TAIL])
        
    def numlify(x):
        return int(x[1])
    
    # lambda 안에서 튜플로 두 조건을 묶어줘야함
    div_file = sorted(div_file, key=lambda x: (x[0].lower(), numlify(x)))
    
    for df in div_file:
        answer.append("".join(df))
    return answer