import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int h = 0;
        
        // 뒤에서부터 읽으면서 i+1편 이상의 논문이 i+1회 이상 인용되었는지 확인
        for (int i = 0; i < n; i++) {
            int cite = citations[n - 1 - i];  
            if (cite >= i + 1) {
                h = i + 1;               // 조건 만족 시 h 갱신
            } else {
                break;                   // 더 이상 만족 못 하면 종료
            }
        }
        
        return h;
    }
}

// h번 이상 인용된 논문이 h편 이상이고
// 나머지 논문이 h번 이하 인용되었다면 h의 최댓값
/*
// 1 1 1 1 1 => 1
1: 5

// 1 2 2 2 2 => 2
1: 1
2: 4

// 1 1 1 2 2 => 1
1: 3
2: 2

// 1 1 1 3 3 => 1
1: 3
3: 2

// 1 1 2 2 2 => 2
1: 2
2: 3

// 1 1 1 2 2 2 => 2 
1: 3
2: 3

// 1 2 2 3 3 3 => 3
1: 1
2: 2
3: 3

// 1 1 1 2 2 3 => 2
1 : 3
2: 2
3: 1

// 1 100 100 100 => 1
1 : 1
100 : 3

// 0 1 3 5 6 => 3

*/