/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1780                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1780                           #+#        #+#      #+#    */
/*   Solved: 2025/01/24 16:45:11 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    static int [][] map;
    // [0]: -1, [1]: 0, [2], 1에 대한 종이 누적 결과값
    static int []result = {0, 0 ,0};
    static int N;

    static RecurResult recur(int nowX, int nowY, int K){
        if(K == 1){
            return new RecurResult(true, map[nowX][nowY]);
        }else{
            int nextK = K / 3;
            // 현재 K의 나머지 K/3 상태를 기록할 임시 RecurResult
            RecurResult[][] tempRecurResult = new RecurResult[3][3];
            for(int i = 0;i < 3;i++)
                for(int j = 0;j < 3;j++)
                    tempRecurResult[i][j] = recur(nowX + (nextK * i), nowY + (nextK * j), nextK);
            
            int[]cnt = {0, 0 ,0};

            // isSame이 true인 항목들에 대해서만
            // KxK 종이에서 각 숫자를 카운트
            // 이때 -1, 0, 1에 대해서 1씩 더한 인덱스 위치에 카운트
            for(int i = 0;i < 3;i++)
                for(int j = 0;j < 3;j++)
                    if(tempRecurResult[i][j].isSame == true)
                        cnt[tempRecurResult[i][j].sameNum + 1] += 1;

            // KxK의 종이의 숫자가 모두 같을 경우
            // sameNum의 경우 해당 인덱스에서 1을 빼서 리턴
            for(int i = 0;i < 3;i ++){
                if(cnt[i] == 9)
                    return new RecurResult(true, i - 1);
            }

            // KxK 종이의 숫자가 모두 다르기 때문에 각각 누적하고 false 리턴
            for(int i = 0;i < 3;i++)
                result[i] += cnt[i];
            return new RecurResult(false, 0);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        map = new int[N + 1][N + 1];
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0;j < N;j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }

        // 모두 같을 때 예외처리
        // 이를 통해 N=1인 경우도 함께 예외처리 가능
        RecurResult recurResult = recur(0, 0, N);
        if(recurResult.isSame == true)
            result[recurResult.sameNum + 1] = 1;

        for(int i = 0;i < 3;i++)
            bw.write("" + result[i] + "\n");
        bw.flush();
    }
}

// 각 재귀 단계의 결과를 위한 객체
class RecurResult{
    // 해당 3^K 종이가 모두 같은지
    public boolean isSame;
    // 해당 3^K 종이가 같다면 어떤 숫자인지
    public int sameNum;

    public RecurResult(boolean isSame, int sameNum){
        this.isSame = isSame;
        this.sameNum = sameNum;
    }
}
