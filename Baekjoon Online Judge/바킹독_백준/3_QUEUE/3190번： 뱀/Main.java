/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 3190                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/3190                           #+#        #+#      #+#    */
/*   Solved: 2024/09/14 11:59:45 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Coord> snake = new LinkedList<>();
        StringTokenizer st;
        // 4 방향에 대한 direction 배열
        Coord[] directions = {new Coord(1, 0), new Coord(0, 1), new Coord(-1, 0), new Coord(0, -1)};
        // -1 : 벽 / 0 : 빈공간 / 1 : 뱀 / 2 : 사과
        int[][] map = new int[110][110];
        int i,j;

        int N,K,L;
        int X = 0;
        // 해당 Time에 맞는 index에 방향을 저장
        // 방향전환 정보는 시간 순으로 주어진다
        char[] cmd = new char[10001];
        // 전체 커맨드 배열 초기화
        for(i = 0;i < 10001;i++){
            cmd[i] = 'N';
        }
        
        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());

        // 맵 초기화, 벽을 101로 초기화
        for(i = 0;i <= N + 1;i++){
            for(j = 0;j <= N + 1;j++){
                if(i == 0 || j == 0 || i == N + 1 || j == N + 1)
                    map[i][j] = -1;
                else
                    map[i][j] = 0;
            }
        }

        for(i = 0;i < K;i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            // 사과의 행렬위치 올바르게 볼 것
            // (x, y) 좌표가 아닌 행/열 위치로 기능해야함
            map[x][y] = 2;
        }

        L = Integer.parseInt(br.readLine());
        for(i = 0;i < L;i++){
            st = new StringTokenizer(br.readLine());
            int time = Integer.parseInt(st.nextToken());
            char command = st.nextToken().charAt(0);
            cmd[time] = command;
        }

        map[1][1] = 1;
        snake.push(new Coord(1, 1));
        Coord next = new Coord(1, 1);
        // 초기에 오른쪽 방향으로 움직임
        int dirIndex = 0;
        Coord dir = directions[0];
        
        while(true){
            X++;
            // 객체 참조 오류
            // Deque에 들어간 객체가 변경되므로 getter/setter가 아닌
            // 새로운 객체로 생성해주어야 한다
            next = new Coord(next.x + dir.x, next.y + dir.y);

            if(map[next.y][next.x] == -1 || map[next.y][next.x] == 1){
                break;
            }else if(map[next.y][next.x] == 2){
                map[next.y][next.x] = 1;
                snake.addLast(next);
            }else{
                Coord tmp = snake.pollFirst();
                map[tmp.y][tmp.x] = 0;
                
                map[next.y][next.x] = 1;
                snake.addLast(next);
            }

            if(cmd[X] == 'L'){
                dirIndex = (dirIndex - 1 + 4) % 4;
            }else if(cmd[X] == 'D'){
                dirIndex = (dirIndex + 1) % 4;
            }
            dir = directions[dirIndex];

            //printMap(map, N, X);
        }

        bw.write(X + "\n");
        bw.flush();
    }

//     // 디버깅을 위한 맵 출력 메소드
//     static void printMap(int[][] map, int N, int X){
//         System.out.println("Time : " + X);
//         for(int i = 0;i <= N + 1;i++){
//             for(int j = 0;j <= N + 1;j++){
//                 if(map[i][j] != -1)
//                     System.out.print(map[i][j] + "  ");
//                 else
//                     System.out.print("-1 ");
//             }
//             System.out.println();
//         }
//         System.out.println();

//         try{
//             Thread.sleep(1000);
//         }catch(InterruptedException e){
//             e.printStackTrace();
//         }
//     }
}

class Coord{
    int x;
    int y;
    Coord(int x, int y){
        this.x = x;
        this.y = y;
    }

    void setX(int x){
        this.x = x;
    }
    void setY(int y){
        this.y = y;
    }
}