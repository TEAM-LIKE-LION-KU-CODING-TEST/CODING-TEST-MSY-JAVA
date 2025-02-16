// Kadane’s Algorithm
// 주어진 배열에서 연속된 부분 배열 중 합이 최대가 되는 부분 배열의 합을 구하는 O(N) 알고리즘
// 최소 평균 Slice 문제에는 적합하지 않지만, 연속된 합을 찾는 다른 문제에서 유용

// 1. 현재 위치까지 최대 부분합을 저장하며 이동한다.
// 2. "이전까지의 최대합 + 현재 값"을 비교하여 더 큰 값을 유지한다.
// 3. 만약 합이 0보다 작아지면, 다시 0으로 초기화한다.
//    => 새로운 부분합을 시작하는 방식으로 최적화를 수행
// * 모든 원소가 음수일 경우 가장 큰 음수를 정답으로 설정해야 함함

class Solution {
    public int solution(int[] A) {
        int max_ending = A[0];   // 첫 번째 원소로 초기화
        int max_sum = A[0]; // 최대 부분합도 첫 번째 원소로 초기화

        for (int i = 1; i < A.length; i++) {
            max_ending = Math.max(A[i], max_ending + A[i]); // 0이 아니라 현재 원소 유지
            max_sum = Math.max(max_sum, max_ending); // 전체 최대 부분합 갱신
        }

        return max_sum;
    }
}
