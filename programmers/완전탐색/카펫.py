def solution(brown, yellow):
    # 높이를 1부터 가로 길이와 세로 길이가 같을때까지 완전탐색
    height = 1
    while True:
        # 나누어지지 않으면 직사각형 불가
        if yellow % height != 0:
            height += 1
            continue
        width = yellow // height
        # 현재 높이의 테두리 1줄 갈색 숫자
        cur_brown = (height * 2) + (width * 2) + 4
        if cur_brown == brown:
            # 반환시 전체 카펫의 크기이므로 각각 + 2
            return [width + 2, height + 2]
        height += 1