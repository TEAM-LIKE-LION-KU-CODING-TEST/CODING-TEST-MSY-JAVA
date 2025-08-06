/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 20125                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/20125                          #+#        #+#      #+#    */
/*   Solved: 2025/07/08 13:26:07 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;

class Main{
    private static int countCookie(int[][]arr, int xPos, int yPos, int dirX, int dirY, int N){
        int cnt = 0;
        while (true) {
            if(xPos > N || yPos > N || xPos < 1 || yPos < 1 || arr[yPos][xPos] != 1)
                return cnt;
           cnt++;
           xPos += dirX;
           yPos += dirY;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        // 0은 빈 공간, 1은 쿠키
        int[][]arr = new int[N + 2][N + 2];
        for(int i = 0;i < N;i++){
            String line = br.readLine();
            for(int j = 0;j < line.length();j++){
                if(line.charAt(j) == '_'){
                    arr[i + 1][j + 1] = 0;
                }else{
                    arr[i + 1][j + 1] = 1;
                }
            }
        }

        // 심장의 위치 찾기
        int heartX = 0;
        int heartY = 0;
        for(int i = 1;i <= N - 2;i++){
            for(int j = 1;j <= N - 1;j++){
                if((arr[i - 1][j] == 1) && (arr[i + 1][j] == 1) &&
                    (arr[i][j + 1] == 1) && (arr[i][j - 1] == 1)){
                        heartX = j;
                        heartY = i;
                    }
            }
        }
        bw.write("" + heartY + " " + heartX + "\n");

        // int[][]arr, int xPos, int yPos, int dirX, int dirY, int N
        // 왼쪽팔
        bw.write("" + countCookie(arr, heartX - 1, heartY, -1, 0, N) + " ");
        // 오른쪽 팔
        bw.write("" + countCookie(arr, heartX + 1, heartY, 1, 0, N) + " ");
        // 허리
        int waist = countCookie(arr, heartX, heartY + 1, 0, 1, N);
        bw.write("" + waist + " ");
        // 왼쪽 다리
        bw.write("" + countCookie(arr, heartX - 1, heartY + waist + 1, 0, 1, N) + " ");
        // 오른쪽 다리
        bw.write("" + countCookie(arr, heartX + 1, heartY + waist + 1, 0, 1, N) + " ");

        bw.flush();
    }
}