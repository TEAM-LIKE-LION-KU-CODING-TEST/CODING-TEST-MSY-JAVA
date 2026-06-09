/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 18258                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/18258                          #+#        #+#      #+#    */
/*   Solved: 2024/09/13 15:04:43 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Integer> que = new LinkedList<>();
        
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if(cmd.equals("push")){
                int num = Integer.parseInt(st.nextToken());
                que.add(num);
            }else if(cmd.equals("pop")){
                if(que.isEmpty())
                    bw.write(-1 + "\n");
                else
                    bw.write(que.poll() + "\n");
            }else if(cmd.equals("size")){
                bw.write(que.size() + "\n");
            }else if(cmd.equals("empty")){
                if(que.isEmpty())
                    bw.write("1\n");
                else
                    bw.write("0\n");
            }else if(cmd.equals("front")){
                if(que.isEmpty())
                    bw.write(-1 + "\n");
                else
                    bw.write(que.peekFirst() + "\n");
            }else if(cmd.equals("back")){
                if(que.isEmpty())
                    bw.write(-1 + "\n");
                else
                    bw.write(que.peekLast() + "\n");
            }
        }
        bw.flush();
    }
}
