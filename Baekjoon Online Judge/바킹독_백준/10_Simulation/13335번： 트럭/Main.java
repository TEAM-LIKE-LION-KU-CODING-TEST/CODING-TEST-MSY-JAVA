/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 13335                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/13335                          #+#        #+#      #+#    */
/*   Solved: 2025/01/31 21:10:11 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 트럭의 개수
        int n = Integer.parseInt(st.nextToken());
        // 다리의 길이
        int w = Integer.parseInt(st.nextToken());
        // 다리의 최대 하중
        int L = Integer.parseInt(st.nextToken());
        int[] trucks = new int[n + 1];

        st = new StringTokenizer(br.readLine());
        for(int i = 0;i < n;i++)
            trucks[i] = Integer.parseInt(st.nextToken());

        Queue<Integer> bridge = new LinkedList<>();
        int currentWeight = 0;
        int time = 0;
        int index = 0;

        for (int i = 0; i < w; i++) {
            bridge.add(0);
        }

        while (!bridge.isEmpty()) {
            time++;
            currentWeight -= bridge.poll();
            
            if (index < n) {
                if (currentWeight + trucks[index] <= L) {
                    bridge.add(trucks[index]);
                    currentWeight += trucks[index];
                    index++;
                } else {
                    bridge.add(0);
                }
            }
        }

        bw.write(time + "\n");
        bw.flush();
    }
}