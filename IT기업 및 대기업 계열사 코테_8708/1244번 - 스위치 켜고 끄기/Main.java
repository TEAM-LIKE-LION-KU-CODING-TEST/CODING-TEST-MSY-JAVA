/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1244                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1244                           #+#        #+#      #+#    */
/*   Solved: 2025/07/10 13:42:12 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    private static int toggle(int tmp){
        if(tmp == 1)
            return 0;
        return 1;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int[]arr = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1;i <= N;i++)
            arr[i] = Integer.parseInt(st.nextToken());

        int P = Integer.parseInt(br.readLine());
        for(int i = 0;i < P;i++){
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());

            if(gender == 1){
                for(int j = num;j <= N;j+=num)
                    arr[j] = toggle(arr[j]);
            }else{
                int iterNum = 1;
                while(true){
                    if((num - iterNum < 1) || (num + iterNum > N))
                        break;
                    if(arr[num - iterNum] != arr[num + iterNum])
                        break;
                    iterNum++;
                }
                arr[num] = toggle(arr[num]);
                for(int j = 1;j < iterNum;j++){
                    arr[num + j] = toggle(arr[num + j]);
                    arr[num - j] = toggle(arr[num - j]);
                }
            }
        }

        for(int i = 1;i <= N;i++){
            bw.write("" + arr[i] + " ");
            if(i % 20 == 0)
                bw.write("\n");
        }
        bw.flush();
    }
}