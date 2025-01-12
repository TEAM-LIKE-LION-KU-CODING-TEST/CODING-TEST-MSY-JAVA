/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10866                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10866                          #+#        #+#      #+#    */
/*   Solved: 2025/01/12 19:27:03 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // ArrayDeque가 LinkedList에 비해 속도가 더 빠르다
        Deque<Integer> deq = new ArrayDeque<>();

        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if(cmd.equals("push_front")){
                int num = Integer.parseInt(st.nextToken());
                deq.addFirst(num);
                continue;
            } else if(cmd.equals("push_back")){
                int num = Integer.parseInt(st.nextToken());
                deq.addLast(num);
                continue;
            } else if(cmd.equals("pop_front")){
                if(deq.isEmpty())
                    bw.write("-1");
                else
                    bw.write("" + deq.removeFirst());
            } else if(cmd.equals("pop_back")){
                if(deq.isEmpty())
                    bw.write("-1");
                else
                    bw.write("" + deq.removeLast());
            } else if(cmd.equals("size")){
                bw.write("" + deq.size());
            } else if(cmd.equals("empty")){
                if(deq.isEmpty())
                    bw.write("1");
                else
                    bw.write("0");
            } else if(cmd.equals("front")){
                if(deq.isEmpty())
                    bw.write("-1");
                else
                    bw.write("" + deq.peekFirst());
            } else if(cmd.equals("back")){
                if(deq.isEmpty())
                    bw.write("-1");
                else
                    bw.write("" + deq.peekLast());
            }
            bw.write("\n");
            bw.flush();
        }
    }
}