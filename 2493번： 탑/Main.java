/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2493                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2493                           #+#        #+#      #+#    */
/*   Solved: 2024/09/13 13:27:09 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Deque<Pair> deq = new ArrayDeque<>();

        int N = Integer.parseInt(br.readLine());
        // ArrayList는 가변적인 특징을 가지고 있으나 Array보다는 느림
        // 따라서 Array로 처리할 수 있을 경우  Array를 사용하는 것이 더 좋음
        int [] nums = new int[N + 10];
        int [] ans = new int[N + 10];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1;i <= N;i++)
            nums[i] = Integer.parseInt(st.nextToken());

        for(int i = N;i >= 1;i--){
            int now = nums[i];
            while(true){
                if(deq.isEmpty()) break;
                if(deq.peek().height > now) break;

                // Poll된 Object를 저장하여 ans 배열에 저장
                Pair tmp = deq.poll();
                ans[tmp.index] = i;
            }
            deq.push(new Pair(now, i));
        }

        while(!deq.isEmpty())
            ans[deq.poll().index] = 0;

        for(int i = 1;i <= N;i++)
            bw.write(ans[i] + " ");
        bw.flush();
    }
}

// Deque (Stack)에서 Poll되는 데이터의 인덱스를 기억해
// 몇번째 탑이 신호를 수신하는지 저장하기 위해 Pair Class 사용
class Pair{
    int height;
    int index;
    Pair(int height, int index){
        this.height = height;
        this.index = index;
    }
}