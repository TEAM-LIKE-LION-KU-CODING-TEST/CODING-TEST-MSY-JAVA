/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 15656                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/15656                          #+#        #+#      #+#    */
/*   Solved: 2025/01/26 21:26:49 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    static int N;
    static int M;
    static int[] arr;
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    // 각 수열이 만들어질 때의 trace를 기록할 Deque
    static Deque<Integer> deq = new ArrayDeque<>();

    static void recur(int idx, int level) throws IOException{
        deq.addLast(arr[idx]);

        // 최하단 레벨에 도착했을 때
        // 현재 수열의 모든 trace 출력
        if(level == M){
            Iterator<Integer> iter = deq.iterator();
            bw.write("" + iter.next());
            while(iter.hasNext())
                bw.write(" " + iter.next());
            bw.write("\n");
            return;
        }
        
        for(int i = 0;i < N;i++){
            recur(i, level + 1);
            // 재귀가 완료되면 removeLast
            deq.removeLast();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0;i < N;i++)
            arr[i] = Integer.parseInt(st.nextToken());
        
        // 입력받은 자연수를 오름차순 정렬
        Arrays.sort(arr);

        for(int i = 0;i < N;i++){
            recur(i, 1);
            deq.removeLast();
        }

        // ⭐ 시간초과를 해결하기 위해 마지막에 flush
        bw.flush();
    }
}