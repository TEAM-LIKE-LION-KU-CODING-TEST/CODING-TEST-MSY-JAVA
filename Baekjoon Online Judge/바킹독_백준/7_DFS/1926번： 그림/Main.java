/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1926                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1926                           #+#        #+#      #+#    */
/*   Solved: 2024/09/25 13:36:21 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Coordinate> stack = new ArrayDeque<>();
        int[] dirx = {1, 0, -1, 0};
        int[] diry = {0, 1, 0, -1};

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int [][]map = new int[n + 2][m + 2];

        // 전체 map을 0으로 초기화
        for(int i = 0;i <= n + 1;i++)
            for(int j = 0;j <= m + 1;j++)
                map[i][j] = 0;

        // nxm 크기의 map을 (1,1) 위치부터 입력받아 저장
        for(int i = 1;i <= n;i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 1;j <= m;j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0;
        int maxSize = 0;
        for(int i = 1;i <= n;i++){
            for(int j = 1;j <= m;j++){
                    if(map[i][j] == 1){
                        // DFS는 여러 갈래의 경우에는
                        // 깊이만 계산하고 너비는 계산할 수 없음
                        // 따라서 nowSize로 너비를 계산
                        int nowSize = 1;
                        map[i][j] = 0;
                        stack.addFirst(new Coordinate(i, j));
                        while (!stack.isEmpty()) { 
                            Coordinate now = stack.peekFirst();

                            boolean flag = false;
                            for(int k = 0;k < 4;k++){
                                int nextX = now.x + dirx[k];
                                int nextY = now.y + diry[k];

                                // 범위를 벗어나는 경우 예외처리
                                if (nextX >= 1 && nextX <= n && nextY >= 1 && nextY <= m && map[nextX][nextY] == 1){
                                    nowSize++;
                                    map[nextX][nextY] = 0;
                                    stack.addFirst(new Coordinate(nextX, nextY));
                                    flag = true;
                                    break;
                                }
                            }
                            if(flag)
                                continue;
                            
                            stack.removeFirst();
                        }
                        
                        if(nowSize > maxSize)
                            maxSize = nowSize;
                        cnt++;
                    }               
                }
            }
            bw.write("" + cnt + "\n" + maxSize);
            bw.flush();
        }
    }

class Coordinate{
    int x;
    int y;

    public Coordinate(int x, int y){
        this.x = x;
        this.y = y;
    }
}


/*
// 갈래로 나뉘어진 반례
5 5
1 0 0 0 0
1 1 1 1 1
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0

1
9
*/