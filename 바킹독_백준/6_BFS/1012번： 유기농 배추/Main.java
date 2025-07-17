/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1012                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1012                           #+#        #+#      #+#    */
/*   Solved: 2025/01/21 22:53:20 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // 4방향 정의
        int[] dirX = {1, -1, 0, 0}; int[] dirY = {0, 0, 1, -1};
        // map 정의 (메모리 초과 방지를 루프 밖에서 정의)
        int[][] map = new int[60][60];
        // deque 정의 (메모리 초과 방지를 루프 밖에서 정의)
        Deque<Pair> deq = new ArrayDeque<Pair>();
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for(int i = 0;i < T;i++){
            st = new StringTokenizer(br.readLine());
            // 가로 길이 (1 ~ 50)
            int M = Integer.parseInt(st.nextToken());
            // 세로 길이 (1 ~ 50)
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            // Map 초기화
            for(int j = 0;j < N + 10;j++)
                for(int k = 0;k < M + 10;k++)
                    map[j][k] = 0;
            
            //  각 BFS의 시작 위치를 찾을 Pair 배열 정의
            Pair[] cabbage = new Pair[K];
            
            for(int j = 0;j < K;j++){
                st = new StringTokenizer(br.readLine());
                // 별도의 검사 코드를 넣지 않기 위해 각 좌표에 + 1
                int x = Integer.parseInt(st.nextToken()) + 1;
                int y = Integer.parseInt(st.nextToken()) + 1;
                cabbage[j] = new Pair(x, y);
                // Map 상에서는 [y][x]로 좌표 반전
                map[y][x] = 1;
            }

            int result = 0;
            for(int j = 0;j < K;j++){
                if(map[cabbage[j].getY()][cabbage[j].getX()] == 0)
                    continue;
                
                deq.addFirst(cabbage[j]);
                map[cabbage[j].getY()][cabbage[j].getX()] = 0;
                while (true) {
                    if(deq.isEmpty())
                        break;
                    
                    Pair nowPair = deq.removeLast();
                    int x = nowPair.getX();
                    int y = nowPair.getY();

                    for(int k = 0;k < 4;k++){
                        int nextX = x + dirX[k];
                        int nextY = y + dirY[k];
                        if(map[nextY][nextX] == 1){
                            deq.addFirst(new Pair(nextX, nextY));
                            // Queue에 넣을 때 방문 표시
                            map[nextY][nextX] = 0;
                        }
                    }
                }
                result++;
            }
            bw.write("" + result + "\n");
        }
        bw.flush();
    }
}

class Pair{
    int x;
    int y;
        
    Pair(int x,int y){
        this.x = x;
        this.y = y;
    }

    public int getX(){
        return x;
    }

    public int getY(){
        return y;
    }
}