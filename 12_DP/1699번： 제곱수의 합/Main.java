/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1699                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1699                           #+#        #+#      #+#    */
/*   Solved: 2025/02/07 14:38:54 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;

class Main{
    static int MAX_VALUE = 987654321;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        
        // 시간제한이 2초이기 때문에 가능
        // dp[i]는 dp[i - <i보다 작은 제곱수>]들 중 최솟값 저장
        int[] dp = new int[N + 10];
        // dp 초기화
        for(int i = 0;i < N + 10;i++)
            dp[i] = MAX_VALUE;
        dp[0] = 0; dp[1] = 1;
        for(int i = 2;i <= N;i++){
            // int형으로 변환하여 소숫점을 버려서
            // 현재 i보다 작은 제곱수의 루트값 중 최댓값을 구한다
            int sqrt = (int) Math.sqrt(i);
            while(sqrt != 0){
                // 제곱수를 하나 더 쓰기 때문에 이전 값에 + 1
                int newVal = dp[i - (sqrt * sqrt)] + 1;
                if(dp[i] > newVal)
                    dp[i] = newVal;
                
                // newVal가 1이라는 의미는 i가 제곱수라는 의미이고
                // 최솟값이기 때문에 바로 break;
                if(newVal == 1)
                    break;
                sqrt--;
            }
        }

        bw.write("" + dp[N]);
        bw.flush();
    }
}