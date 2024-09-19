/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 5430                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/5430                           #+#        #+#      #+#    */
/*   Solved: 2024/09/19 18:11:14 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for(int i = 0;i < T;i++){
            // ArrayDeque가 LinkedList에 비해 속도가 더 빠르다
            Deque<String> deq = new ArrayDeque<>();
            String cmd = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String input = br.readLine();

            // ⭐데이터를 입력받는 부분에서 최적화 필요
            // 하나씩 charAt으로 조회하는 것은 더 느리다
            // 따라서 substring 메소드와 split을 이용해서 입력
            input = input.substring(1, input.length() - 1);
            String[] arr = input.split(",");
            if(n > 0)
                for(String s : arr)
                    deq.addLast(s);

            int isFirst = 1;
            for(int j = 0;j < cmd.length();j++){
                if(cmd.charAt(j) == 'R'){
                    isFirst *= -1;
                } else{
                    if(deq.isEmpty()){
                        isFirst = 0;
                        break;
                    } else if(isFirst == 1){
                        deq.removeFirst();
                    }else{
                        deq.removeLast();
                    }
                }
            }
            if(isFirst == 0){
                bw.write("error\n");
                continue;
            }

            bw.write("[");
            Iterator<String> iter = deq.iterator();
            if(isFirst == -1)
                iter = deq.descendingIterator();
            
            if(!deq.isEmpty())
                bw.write(iter.next() + "");
            while(iter.hasNext())
                bw.write("," + iter.next());
            bw.write("]\n");
        }
        bw.flush();
    }
}