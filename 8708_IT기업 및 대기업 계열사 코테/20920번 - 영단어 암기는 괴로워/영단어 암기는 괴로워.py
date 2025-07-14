#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20920                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20920                          #+#        #+#      #+#     #
#    Solved: 2025/07/14 13:34:43 by judemin       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import Counter
# 빠른 출력을 위해 기본 print 함수 대신
# sys.stdout.write를 사용하도록 덮어씌우기기
print = sys.stdout.write

def main():
    # 빠른 입력을 위해 input 대신 sys.stdin.readline 함수를 사용
    N, M = map(int, sys.stdin.readline().rstrip().split())

    words = []
    for _ in range(N):
        word = sys.stdin.readline().rstrip()
        # M보다 짧은 단어 제외
        if len(word) >= M:
            words.append(word)

    # 단어 빈도 계산
    # Counter는 iterable을 받아 각 요소의 빈도를 딕셔너리 형태로 반환
    word_counts = Counter(words)

    # 단어 목록 중복 제거
    # set으로 변환하여 중복을 제거하고 다시 리스트로 변환
    unique_words = list(word_counts.keys())

    # 우선순위에 따라 단어 정렬
    # sorted() 함수에 lambda를 사용하고 정렬 키를 튜플로 구성하여 여러 조건 동시 적용
    # -x[1]: 빈도 (내림차순)
    # -len(x[0]): 길이 (내림차순)
    # x[0]: 알파벳 순 (오름차순)
    # 정렬 기준의 우선순위는 튜플 내 요소의 순서에 따름
    # 각 단어에 대해 (단어, 빈도) 형태의 튜플을 만들고 정렬
    sorted_words = sorted(
        unique_words, 
        # key 인자에는 각 요소를 정렬하기 전에 어떤 값으로 변환할지를 알려주는 함수를 넘겨줌

        # lambda는 이름이 없는 작은 함수를 만들 때 사용
        # lambda 인수: 표현식
        #   인수: 함수가 받을 입력
        #   표현식: 인수를 가지고 수행할 작업, 이 표현식의 결과가 반환
        # lambda x: x * 2는 def func(x): return x * 2와 같은 역할을 하는 함수를 그 자리에서 만든다고 생각하면 됨

        # 여기서 가장 중요한 부분은 key 함수가 반환하는 값이 튜플이라는 점
        # 파이썬은 튜플을 정렬할 때, 튜플의 첫 번째 요소부터 순서대로 비교
        key=lambda word: (
            # 1. 자주 나오는 단어일수록 앞에 배치한다.
            # 파이썬은 기본적으로 오름차순으로 정렬하기 때문에
            # 단어의 빈도수가 높을수록 (절댓값이 클수록) 음수는 작아짐 = 즉 앞에 옴
            -word_counts[word], 
            # 2. 해당 단어의 길이가 길수록 앞에 배치한다.
            -len(word), 
            # 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
            word
        )
    )

    for word in sorted_words:
        print(word + "\n")

if __name__ == "__main__":
    main()