/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 11723                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/11723                          #+#        #+#      #+#    */
/*   Solved: 2025/07/03 13:36:19 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.StringTokenizer;

class Main{
    private static void all(int[]S){
        for(int i = 1;i <= 20;i++)
            S[i] = 1;
    }

    private static void empty(int[]S){
        for(int i = 1;i <= 20;i++)
            S[i] = 0;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[]S = new int[21];
        int M = Integer.parseInt(br.readLine());

        empty(S);
        for(int i = 0;i < M;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String operation = st.nextToken();
            int operand;
            switch (operation) {
                case "add":
                    operand = Integer.parseInt(st.nextToken());
                    S[operand] = 1;
                    break;
                case "remove":
                    operand = Integer.parseInt(st.nextToken());
                    S[operand] = 0;
                    break;
                case "check":
                    operand = Integer.parseInt(st.nextToken());
                    bw.write("" + S[operand] + "\n");
                    break;
                case "toggle":
                    operand = Integer.parseInt(st.nextToken());
                    if(S[operand] == 1)
                        S[operand] = 0;
                    else
                        S[operand] = 1;
                    break;
                case "all":
                    all(S);
                    break;
                default:
                    empty(S);
                    break;
            }
        }
        bw.flush();
    }
}