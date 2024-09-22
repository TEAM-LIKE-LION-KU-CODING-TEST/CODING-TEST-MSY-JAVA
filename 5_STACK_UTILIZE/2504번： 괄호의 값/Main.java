/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2504                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2504                           #+#        #+#      #+#    */
/*   Solved: 2024/09/20 16:54:23 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Character> deq = new ArrayDeque<>();
        int ans[] = new int[20];

        int i;
        int nowLayer = 0;
        boolean isSum = false;
        String str = br.readLine();
        for(i = 0;i < str.length();i++){
            char now = str.charAt(i);
            if((deq.isEmpty() && (now  == ')' || now  == ']'))){
                bw.write('0');
                break;
            }else if(!deq.isEmpty()){
                if((deq.peekFirst() == '(' && now == ']') ||
                    (deq.peekFirst() == '[' && now == ')')){
                        bw.write('0');
                        break;
                }
            }

            if(now == '(' || now == '['){
                isSum = true;
                nowLayer++;
                deq.addFirst(now);
            } else{
                int num = 2;
                if(now == ']')
                    num = 3;

                if(isSum == true){
                    isSum = false;
                    ans[nowLayer--] += num;
                }else{
                    ans[nowLayer] += ans[nowLayer + 1] * num;
                    ans[nowLayer + 1] = 0;
                    nowLayer--;
                }
                deq.removeFirst();
            }
        }
        
        if(i == str.length())
            bw.write(ans[1] + "\n");
        bw.flush();
    }
}