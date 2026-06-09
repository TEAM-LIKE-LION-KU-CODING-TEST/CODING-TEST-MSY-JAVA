/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10431                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10431                          #+#        #+#      #+#    */
/*   Solved: 2025/07/04 12:28:46 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    // idx와 idx - 1을 swap
    private static void swap(int[] arr, int idx){
        if(idx == 0)
            return;
        int tmp = arr[idx];
        arr[idx] = arr[idx - 1];
        arr[idx - 1] = tmp;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int P = Integer.parseInt(br.readLine());

        for(int i = 0;i < P;i++){
            int answer = 0;
            int[]arr = new int[21];
            // StringTokenizer는 java.util.*의 Class
            StringTokenizer st = new StringTokenizer(br.readLine());
            // 테스트케이스 번호 flush
            st.nextToken();
            // 첫번째 학생은 무조건 세워두기
            int num = Integer.parseInt(st.nextToken());
            arr[0] = num;
            for(int j = 1;j < 20;j++){
                int idx = -1;
                num = Integer.parseInt(st.nextToken());
                arr[j] = num;
                // 자기 앞에 자기보다 키가 큰 학생이 있는지 찾기
                for(int k = j - 1;k >= 0;k--)
                    if(arr[k] > num)
                        idx = k;
                // 자기 앞에 자기보다 키가 큰 학생이 없다면
                if(idx == -1)
                    continue;
                // 자기 앞에 자기보다 키가 큰 학생이 있다면
                for(int k = j;k > idx;k--){
                    swap(arr, k);
                    answer++;
                }
            }
            bw.write("" + (i + 1) + " " + answer + "\n");
        }
        bw.flush();
    }
}

/*
1
1 19 20 17 18 15 16 13 14 11 12 9 10 7 8 5 6 3 4 1 2

Answer
1 180
*/