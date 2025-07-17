/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 4949                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/4949                           #+#        #+#      #+#    */
/*   Solved: 2025/01/20 22:16:02 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

public class Main{
    static int MAX = 987654321;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while(true){
            boolean flag = true;
            Deque<Character> deq = new ArrayDeque<>();
            String input = br.readLine();

            if(input.equals("."))
                break;

            for(int i = 0;i < input.length();i++){
                if(input.charAt(i) == '(' || input.charAt(i) == '['){
                    deq.addFirst(input.charAt(i));
                }else if(input.charAt(i) == ')'){
                    if(deq.isEmpty() || deq.peekFirst() == '['){
                        flag = false;
                        break;
                    } else
                        deq.removeFirst();
                }else if(input.charAt(i) == ']'){
                    if(deq.isEmpty() || deq.peekFirst() == '(') {
                        flag = false;
                        break;
                    } else
                        deq.removeFirst();
                }
            }
            if(!deq.isEmpty() || flag == false)
                bw.write("no\n");
            else
                bw.write("yes\n");
            bw.flush();
        }
    }
}