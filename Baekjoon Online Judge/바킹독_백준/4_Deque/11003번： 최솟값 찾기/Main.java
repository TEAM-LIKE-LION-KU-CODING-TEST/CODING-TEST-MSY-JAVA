/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 11003                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/11003                          #+#        #+#      #+#    */
/*   Solved: 2024/09/18 21:23:40 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
// Sliding Window
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Pair> deq = new LinkedList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Pair[] arr = new Pair[N + 10];
        for(int i = 1;i <= N;i++)
            arr[i] = new Pair(Integer.parseInt(st.nextToken()), i);

        for(int i = 1;i <= N;i++){
            // ⭐현재 최솟값이 나갈 순서가 되면 remove
            if(!deq.isEmpty() && deq.peekFirst().idx + L == i)
                deq.removeFirst();
            
            while(!deq.isEmpty() && deq.peekLast().num > arr[i].num)
                deq.removeLast();
            
            deq.addLast(arr[i]);
            bw.write(deq.peekFirst().num + " ");
        }
        bw.flush();
    }
}

// 나갈 순서를 기억하고 처리하기 위해 필요
class Pair{
    int num;
    int idx;

    public Pair(int num, int idx){
        this.num = num;
        this.idx = idx;
    }
}