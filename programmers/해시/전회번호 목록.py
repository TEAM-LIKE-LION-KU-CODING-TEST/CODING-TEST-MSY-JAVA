def solution(phone_book):
    # 전화번호를 사전순으로 정렬
    phone_book.sort()
    # 사전순으로 정렬된 전화번호에 대해 k, k+1만 비교
    for i in range(len(phone_book) - 1):
        # 내장 startswith() 함수 사용
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True