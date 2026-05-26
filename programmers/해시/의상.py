def solution(clothes):
    answer = 1
    # 의상의 종류에 따른 개수 딕셔너리 생성
    dict = {}
    for c in clothes:
        dict[c[1]] = dict.get(c[1], 0) + 1
    # 안 입는 경우 1개, 입는 경우 개수를 더해 조합의 수 구하기
    for value in dict.values():
        answer *= (value + 1)
    # 아무것도 입지 않는 하나를 빼서 최종 결과 반환
    return answer - 1