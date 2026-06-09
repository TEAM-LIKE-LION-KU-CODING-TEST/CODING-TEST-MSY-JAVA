/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1799                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1799                           #+#        #+#      #+#    */
/*   Solved: 2024/10/28 19:10:46 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());

        int [][]map = new int[N + 1][N + 1];
        for(int i = 1;i <= N;i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 1;j <= N;j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }

        BishopProcess bp = new BishopProcess();
        bp.setN(N);
        bp.setIsWhite(false);
        bp.bishop(map, 1, 1, 0);
        // 검은색의 경우 놓을 수 있는 최대 저장
        int blackMax = bp.getMax();

        // max값을 초기화
        bp.initMax();
        bp.setIsWhite(true);
        bp.bishop(map, 2, 1, 0);

        System.out.println(blackMax + bp.getMax());
    }
}

class BishopProcess{
    int []dirX = {-1, 1, -1, 1};
    int []dirY = {-1, -1, 1, 1};
    int N = 0;
    int max = 0;
    boolean isWhite = false;

    void setN(int N){
        this.N = N;
    }

    int getMax(){
        return max;
    }

    void initMax(){
        this.max = 0;
    }

    void setIsWhite(boolean isWhite){
        this.isWhite = isWhite;
    }

    boolean isOutBound(int x, int y){
        if(x > N || y > N || x < 1 || y < 1)
            return true;
        return false;
    }

    void printMap(int[][]map){
        for(int i = 1;i <= N;i++){
            for(int j = 1;j <= N;j++)
                System.out.print(map[i][j] + " ");
            System.out.println();
        }
        System.out.println();
    }

    // map[][] : 0 : can't, 1 : can, 2:Bishop
    void bishop(int[][]map, int nowX, int nowY, int cnt){
        // 종료조건 : (N + 1, x)에 도달했을 때
        // 즉, map의 모든 좌표에 대해 순회 완료
        if(nowY >= N + 1){
            // Max값과 cnt 값 비교
            if(max < cnt){
                max = cnt;
                // System.out.println(isWhite);
                // printMap(map);
            }
            return;
        }

        // 현재 자리에 비숍을 놓는 것이 가능한지 검사
        boolean canPlace = true;
        if(map[nowY][nowX] == 0)
            canPlace = false;
        
        for(int i = 0;i < 4;i++){
            if(!canPlace)
                break;
            
            int tmpX = nowX + dirX[i];
            int tmpY = nowY + dirY[i];
            while(!isOutBound(tmpX, tmpY)){
                if(map[tmpY][tmpX] == 2){
                    canPlace = false;
                    break;
                }

                tmpX = tmpX + dirX[i];
                tmpY = tmpY + dirY[i];
            }
        }

        // 다음 위치로 이동
        // 가로축으로 1씩 이동하다가
        // 가로 끝에 도달하면 세로 축으로 1이동
        int nextX = nowX + 2;
        int nextY = nowY;
        if(nextX > N){
            if(isWhite == false){
                nextX = 2;
                if(nowY % 2 == 0)
                    nextX = 1;
            }else{
                nextX = 1;
                if(nowY % 2 == 0)
                    nextX = 2;
            }
            nextY += 1;
        }

        // 현재 자리에 비숍을 놓는 경우
        if(canPlace){
            map[nowY][nowX] = 2;
            bishop(map, nextX, nextY, cnt + 1);
            // map을 비숍을 놓지 않은 상태로 돌려놓기
            map[nowY][nowX] = 1;
        }

        // 현재 자리에 비숍을 놓지 않는 경우
        bishop(map, nextX, nextY, cnt);
    }
}

/*
3
0 1 0
1 0 1
0 0 0

2
*/