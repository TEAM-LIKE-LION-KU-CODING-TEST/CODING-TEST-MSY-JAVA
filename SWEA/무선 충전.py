def is_out(y, x):
    if y < 1 or y > 10 or x < 1 or x > 10:
        return True
    return False

def set_ap(phone_map, ap, num):
    x, y, C, P = ap
    for i in range(y - C, y + C + 1):
        if i < 1 or i > 10:
            continue
        for j in range(x - (C - abs(y - i)), x + (C - abs(y - i)) + 1):
            if j < 1 or j > 10:
                continue
            phone_map[i][j].append(num)

def get_max(ap, ap_list):
    result = -1
    for al in ap_list:
        result = max(result, ap[al][3])
    return result

T = int(input())
# y, x 기준 처리
directions = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
for t in range(T):
    answer = 0
    M, A = map(int, input().split())
    ma = list(map(int, input().split()))
    mb = list(map(int, input().split()))
    
    AP = []
    phone_map = [[[] for _ in range(12)] for _ in range(12)]
    for i in range(A):
        # (x, y), C, P
        AP.append(list(map(int, input().split())))
        set_ap(phone_map, AP[i], i)

    # for pm in phone_map:
    #     print(pm)

    # y, x 기준 좌표
    ca = [1, 1]
    cb = [10, 10]
    for m in range(M + 1):
        a_available = set(phone_map[ca[0]][ca[1]])
        b_available = set(phone_map[cb[0]][cb[1]])

        # 나누어서 충전해야할 경우 = 오직 두 사람 모두 하나만 접근 가능, BC도 동일
        if len(a_available | b_available) == 1 and len(a_available ^ b_available) == 0:
            answer += AP[list(a_available)[0]][3]
        elif  len(a_available & b_available) != 0:
            # 교집합이 있는 경우
            tmp_ans = -1
            inter = a_available & b_available
            tmp_ans = max(tmp_ans, get_max(AP, inter) + get_max(AP, a_available - inter))
            tmp_ans = max(tmp_ans, get_max(AP, inter) + get_max(AP, b_available - inter))
            tmp_ans = max(tmp_ans, get_max(AP, a_available - inter) + get_max(AP, b_available - inter))
            if len(inter) != 1:
                inter_list = []
                for i in inter:
                    inter_list.append(AP[i][3])
                inter_list.sort()
                tmp_ans = max(tmp_ans, inter_list[-1] + inter_list[-2])
            answer += tmp_ans
        else:
            # 교집합이 없는경우, 두개 모두 빈 경우, 둘 모두 빈 경우도 해당
            if a_available:
                answer += get_max(AP, a_available)
            if b_available:
                answer += get_max(AP, b_available)

        # print(m, ca, cb, answer)

        if m == M:
            break
        ca[0] += directions[ma[m]][0]
        ca[1] += directions[ma[m]][1]
        cb[0] += directions[mb[m]][0]
        cb[1] += directions[mb[m]][1]

    print(f"#{t + 1} {answer}")
