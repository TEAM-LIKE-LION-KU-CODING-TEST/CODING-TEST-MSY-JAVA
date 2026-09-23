from collections import deque

T = int(input())

def selection(n, num_list, ex_limit):
    queue = deque([(num_list[:], 0, 0)])
    max_ex_cnt = 0
    final_candidates = []

    while queue:
        curr_list, i, ex_cnt = queue.popleft()
        max_ex_cnt = max(max_ex_cnt, ex_cnt)

        # 목표 교환 횟수를 채웠거나, 모든 자릿수를 다 확인했다면 최종 후보에 추가
        if ex_cnt == ex_limit or i == n:
            final_candidates.append((curr_list, ex_cnt))
            continue

        # 현재 자릿수부터 남은 범위에서 최댓값 찾기
        max_val = max(curr_list[i:])
        
        # 이미 i번째 자리가 남은 범위 내 최댓값이라면 교환 없이 다음 자리로 진행
        if curr_list[i] == max_val:
            queue.append((curr_list, i + 1, ex_cnt))
            continue

        # 최댓값과 같은 값을 가진 뒤쪽의 모든 인덱스를 찾아서 각각 교환 시도
        for j in range(i + 1, n):
            if curr_list[j] == max_val:
                next_list = curr_list[:]
                next_list[i], next_list[j] = next_list[j], next_list[i]
                queue.append((next_list, i + 1, ex_cnt + 1))

    # 탐색된 최종 리스트 중 사전순으로 가장 큰 값을 선택
    final_candidates.sort(key=lambda x: x[0], reverse=True)
    best_list, best_ex_cnt = final_candidates[0]
    
    # 원본 num_list를 가장 좋은 결과로 덮어쓰기
    for idx in range(n):
        num_list[idx] = best_list[idx]
        
    return best_ex_cnt

for c in range(T):
    num, ex_limit = map(int, input().split())
    num_list = []
    while num > 0:
        num_list.append(num % 10)
        num //= 10
    num_list = num_list[-1::-1]
    n = len(num_list)
    
    ex_cnt = selection(n, num_list, ex_limit)
    
    if ex_cnt < ex_limit:
        ex_left = ex_limit - ex_cnt
        if ex_left % 2 != 0:
            if len(set(num_list)) == n:
                num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
                
    answer = ""
    for n_val in num_list:
        answer += str(n_val)
    print(f"#{c + 1} {answer}")
