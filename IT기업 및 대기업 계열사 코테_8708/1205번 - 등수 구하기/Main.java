/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1205                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1205                           #+#        #+#      #+#    */
/*   Solved: 2025/07/09 11:53:14 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long score = Long.parseLong(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        if (N == 0) {
            bw.write("1");
            bw.flush();
            return;
        }

        Long[] board = new Long[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++)
            board[i] = Long.parseLong(st.nextToken());

        if (N == P && score <= board[N - 1]) {
            bw.write("-1");
            bw.flush();
            return;
        }

        board[N] = score;
        // 내림차순 정렬
        Arrays.sort(board, Collections.reverseOrder());

        int[] rank = new int[N + 1];
        int curRank   = 1;
        int cumulate  = 1;
        long curScore = board[0];
        rank[0] = curRank;
        for (int i = 1; i <= N; i++) {
            if (board[i] == curScore) {
                cumulate++;
            } else {
                curRank += cumulate;
                curScore = board[i];
                cumulate = 1;
            }
            rank[i] = curRank;
        }

        for (int i = 0; i <= N; i++) {
            if (board[i] == score) {
                if (i >= P) {
                    bw.write("-1");
                } else {
                    bw.write(String.valueOf(rank[i]));
                }
                break;
            }
        }

        bw.flush();
    }
}