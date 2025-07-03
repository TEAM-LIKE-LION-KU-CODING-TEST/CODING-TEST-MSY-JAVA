/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2816                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2816                           #+#        #+#      #+#    */
/*   Solved: 2025/07/03 12:52:17 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;

// 그리디
// 굳이 최소한의 버튼만으로 KBS1과 KBS2를 옮길 필요가 없음
class Main{
    private static void swap(String[]arr, int src, int dst){
        String tmp = arr[src];
        arr[src] = arr[dst];
        arr[dst] = tmp;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        String[]channels = new String[N];

        for(int i = 0;i < N;i++)
            channels[i] = br.readLine();

        // 1. KBS1을 찾는다
        int idx = 0;
        while(!channels[idx].equals("KBS1")){
            bw.write("1");
            idx++;
        }
        // 2. KBS1을 0으로 올린다
        while(!channels[0].equals("KBS1")){
            bw.write("4");
            swap(channels, idx, idx - 1);
            idx--;
        }
        // 3. KBS2를 찾는다
        while(!channels[idx].equals("KBS2")){
            bw.write("1");
            idx++;
        }
        // 4. KBS2를 1로 올린다
        while(!channels[1].equals("KBS2")){
            bw.write("4");
            swap(channels, idx, idx - 1);
            idx--;
        }
        bw.flush();
    }
}