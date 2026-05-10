def solution(progresses, speeds):
    answer = []
    
    days_left = []
    for i in range(len(progresses)):
        tmp = (100 - progresses[i]) // speeds[i]
        if ((100 - progresses[i]) % speeds[i]) != 0:
            tmp += 1
        days_left.append(tmp)
    
    deploy_day = days_left[0]
    count = 0
    for day in days_left:
        if day <= deploy_day:
            # 기준일보다 빨리 끝나면 함께 배포
            count += 1
        else:
            # 기준일보다 늦게 끝나면 이전 그룹 배포 후 기준일 갱신
            answer.append(count)
            count = 1
            deploy_day = day
            
    # 마지막 남은 그룹 추가
    answer.append(count)
    
    return answer