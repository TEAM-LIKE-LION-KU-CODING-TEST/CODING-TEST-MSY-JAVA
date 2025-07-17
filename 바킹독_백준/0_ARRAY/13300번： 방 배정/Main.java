/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 13300                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/13300                          #+#        #+#      #+#    */
/*   Solved: 2025/01/01 21:47:29 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // [7][] 1 ~ 6 : 각 학년
        // [][2] 0 ~ 1 : 성별
        int[][] arr = new int[7][2];
        int answer = 0;

        for(int i = 0;i < 7;i++)
            for(int j = 0;j < 2;j++)
                arr[i][j] = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int grade = Integer.parseInt(st.nextToken());
            arr[grade][gender] += 1;
        }

        for(int i = 1;i <= 6;i++){
            for(int j = 0;j <= 1;j++){
                if(arr[i][j] == 0)
                    continue;
                
                answer += arr[i][j] / K;
                arr[i][j] %= K;

                if(arr[i][j] != 0)
                    answer += 1;
            }
        }

        System.out.println(answer);
    }
}