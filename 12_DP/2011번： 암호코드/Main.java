/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2011                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2011                           #+#        #+#      #+#    */
/*   Solved: 2024/11/12 12:11:00 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String password = br.readLine();
        int n = password.length();
        // dp[n] : n번째 숫자까지 검사했을 때 나오는 경우의 수
        int[] dp = new int[n + 1];
        char[] ch = new char[n + 1];
        for(int i = 1; i <= n; i++) {
            ch[i] = password.charAt(i-1);
        }

        dp[0] = 1;
        for(int i = 1; i <= n; i++) {
            // [i]가 알파벳 하나인 경우
            int num = ch[i] - '0';
            if(1 <= num && num <= 9) {
                // 1개 이동
                dp[i] = dp[i-1];
                dp[i] %= 1000000;
            }

            if(i == 1)
                continue;

            // [i-1]+[i] 두 개를 합친게 알파벳 하나인 경우 (10~26)
            num = (ch[i-1] - '0') * 10 + (ch[i] - '0');
            if(10 <= num && num <= 26) {
                // 2개 전의 데이터를 누적
                dp[i] += dp[i-2];
                dp[i] %= 1000000;
            }
        }

        // bw에서 Int 형태로 출력해주기 위해
        // "" 붙여서 출력
        bw.write(dp[n] + "");
        bw.flush();
    }
}