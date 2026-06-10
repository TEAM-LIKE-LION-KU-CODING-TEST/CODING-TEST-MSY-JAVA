def solution(routes):
    # 진출 지점 기준으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    
    # 첫 번째 카메라 위치를 가장 빨리 나가는 차량의 진출 지점으로 설정
    answer = 0
    camera_pos = -30001
    
    for st, ed in routes:
        # 현재 차량의 진입 지점이 마지막 카메라 위치보다 뒤에 있다면
        # 카메라가 이 차량을 커버하지 못하므로 새로운 카메라 설치
        if st > camera_pos:
            answer += 1
            # 새로운 카메라 위치는 커버하지 못하는 차량의 진출 지점
            camera_pos = ed
            
    return answer