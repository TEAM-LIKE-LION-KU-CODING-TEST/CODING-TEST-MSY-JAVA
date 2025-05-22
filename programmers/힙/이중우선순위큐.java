import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        // <값, 빈도수> 저장
        TreeMap<Integer, Integer> map = new TreeMap<>();
        
        for (String op : operations) {
            String[] parts = op.split(" ");
            String cmd = parts[0];
            int num = Integer.parseInt(parts[1]);
            
            if (cmd.equals("I")) {
                // 삽입
                map.put(num, map.getOrDefault(num, 0) + 1);
                
            } else if (!map.isEmpty()) {
                // 삭제 연산 (빈 큐면 무시)
                int key = (num == 1)
                    ? map.lastKey()   // 최댓값
                    : map.firstKey(); // 최솟값
                
                // 빈도수 감소 또는 키 제거
                int cnt = map.get(key);
                if (cnt == 1) {
                    map.remove(key);
                } else {
                    map.put(key, cnt - 1);
                }
            }
        }
        
        // 결과 반환
        if (map.isEmpty()) {
            return new int[]{0, 0};
        } else {
            return new int[]{map.lastKey(), map.firstKey()};
        }
    }
}
