/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 13305                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/13305                          #+#        #+#      #+#    */
/*   Solved: 2025/07/12 18:02:56 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] distances = new long[N - 1];
        for (int i = 0; i < N - 1; i++) {
            distances[i] = Long.parseLong(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        long[] prices = new long[N];
        for (int i = 0; i < N; i++) {
            prices[i] = Long.parseLong(st.nextToken());
        }

        // 최소 비용 계산
        long totalCost = 0;
        long minPrice = prices[0]; // 첫 번째 도시의 주유 가격을 최소 가격으로 초기 설정

        // 첫 번째 도시부터 N-2번째 도시까지 (즉, N-1개의 도로를 건너기 위해 N-1번 주유)
        // 마지막 도시는 도착지이므로 주유할 필요 없음 (distances 배열의 크기가 N-1인 이유)
        for (int i = 0; i < N - 1; i++) {
            // 현재 도시의 주유 가격이 지금까지 지나온 도시 중 가장 싼 가격보다 저렴하면 갱신
            // 이 원리에 따라, 현재 도시의 가격이 더 싸면 minPrice를 업데이트하여 이후 주유에 반영
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            
            // 현재까지의 최소 가격으로 다음 도로 길이만큼 주유
            totalCost += minPrice * distances[i];
        }

        bw.write(String.valueOf(totalCost));
        bw.newLine();

        bw.flush();
        br.close();
        bw.close();
    }
}