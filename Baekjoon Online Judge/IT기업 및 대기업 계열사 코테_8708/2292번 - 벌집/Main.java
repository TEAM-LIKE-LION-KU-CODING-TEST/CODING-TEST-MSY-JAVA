/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2292                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2292                           #+#        #+#      #+#    */
/*   Solved: 2025/06/30 13:47:17 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;

class Main{
    static long MAX = 1000000000;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());
        long i = 1;
        long cumulate = 6;
        int layer = 1;

        while(N > i && i < MAX){
            i += cumulate;
            cumulate += 6;
            layer += 1;
        }

        System.out.println(layer);
    }
}