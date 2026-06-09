/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 3986                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/3986                           #+#        #+#      #+#    */
/*   Solved: 2024/09/22 19:26:32 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        int ans = 0;
        for(int i = 0;i < N;i++){
            String str = br.readLine();
            Deque<Character> deq = new ArrayDeque<>();
            for(int j = 0;j < str.length();j++){
                char now = str.charAt(j);
                if(deq.isEmpty()){
                    deq.addFirst(now);
                    continue;
                }

                if(deq.peekFirst() == 'A' && now == 'A'){
                    deq.removeFirst();
                } else if(deq.peekFirst() == 'B' && now == 'B'){
                    deq.removeFirst();
                }else {
                    deq.addFirst(now);
                }
            }
            // 별도의 조건 검사가 필요 없음
            // deq에 값이 남아있다면 좋은 단어가 아님
            if(deq.isEmpty())
                ans++;
        }
        bw.write(ans + "\n");
        bw.flush();
    }
}