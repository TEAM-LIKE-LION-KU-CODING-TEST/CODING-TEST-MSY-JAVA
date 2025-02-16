// simple1
// first simple test ✘WRONG ANSWER
// got 0 expected 2
import java.util.*;

class Solution {
    public int solution(int[] A) {
        int N = A.length;
        
        // 1. 봉우리 찾기
        List<Integer> peaks = new ArrayList<>();
        for (int i = 1; i < N - 1; i++) {
            if (A[i - 1] < A[i] && A[i] > A[i + 1]) {
                peaks.add(i);
            }
        }

        // 봉우리가 없거나 하나만 있으면 깃발 1개만 가능
        if (peaks.size() <= 1) return peaks.size();

        // 2. 이진 탐색으로 최대 깃발 개수 찾기
        int left = 1, right = peaks.size();
        int result = 0;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (canPlaceFlags(peaks, mid)) {
                result = mid;
                left = mid + 1; // 더 큰 K를 찾아본다
            } else {
                right = mid - 1; // K를 줄여본다
            }
        }

        return result;
    }

    // 3. 깃발 배치 가능 여부 확인 (Greedy)
    private boolean canPlaceFlags(List<Integer> peaks, int K) {
        int count = 1;
        int lastPosition = peaks.get(0);

        for (int i = 1; i < peaks.size(); i++) {
            if (peaks.get(i) - lastPosition >= K) {
                count++;
                lastPosition = peaks.get(i);
                if (count == K) return true; // 최대 K개 배치 가능
            }
        }
        return false;
    }
}