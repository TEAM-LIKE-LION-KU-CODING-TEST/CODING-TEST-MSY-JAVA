/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 3015                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/3015                           #+#        #+#      #+#    */
/*   Solved: 2024/09/15 16:03:38 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Pair> deq = new ArrayDeque<>();
        long ans = 0;
        int i = 0;

        int N = Integer.parseInt(br.readLine());
        Pair[] arr = new Pair[N + 10];

        for(i = 0;i < N;i++)
            arr[i] = new Pair(Integer.parseInt(br.readLine()), 1);
        
        i = 0;
        while(i < N){
            int height = arr[i].height;

            if(deq.isEmpty()){
                deq.addFirst(arr[i]);
                i++;
            }else if(deq.peekFirst().height == height){
                Pair tmp = deq.removeFirst();
                ans += tmp.count;
                arr[i].addCount(tmp.count);
            }else if(deq.peekFirst().height > height){
                ans++;
                deq.addFirst(arr[i]);
                i++;
            }else{
                Pair tmp = deq.removeFirst();
                ans += tmp.count;
            }
        }
        
        bw.write(ans + "\n");
        bw.flush();
    }
}

class Pair{
    int height;
    int count;

    Pair(int height, int count){
        this.height = height;
        this.count = count;
    }

    void addCount(int n){
        this.count += n;
    }
}