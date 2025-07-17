/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2448                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2448                           #+#        #+#      #+#    */
/*   Solved: 2024/10/27 17:58:20 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    static int map[][];

    static void printStar(int now, int y, int x){
        map[y][x] = 1;
        map[y + 1][x - 1] = 1;
        map[y + 1][x + 1] = 1;
        for(int i = 0; i < 5;i++)
            map[y + 2][x - 2 + i] = 1;
        
        if(now == 1){
            return;
        }

        for(int i = now;i > 1;i = i / 2){
            printStar(i / 2, y + i, x + i);
            printStar(i / 2, y + i, x - i);
        }
    }

    public static void main(String [] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = sc.nextInt();
        map = new int[N + 10][(N * 2) + 10];

        printStar(N / 2, 0, N);
        for(int i = 0;i < N;i++){
            for(int j = 1;j < N * 2;j++){
                if(map[i][j] == 1)
                    bw.write("*");
                else
                    bw.write(" ");
            }
            bw.write("\n");
            bw.flush();
        }
    }
}