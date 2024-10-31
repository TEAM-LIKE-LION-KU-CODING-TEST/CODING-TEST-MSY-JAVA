/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 17136                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/17136                          #+#        #+#      #+#    */
/*   Solved: 2024/10/31 19:51:51 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[]args) throws IOException{
        Paper paper = new Paper();
        paper.backTracking(1, 1, 0);
        if(paper.getMin() == Integer.MAX_VALUE)
            System.out.println("-1");
        else
            System.out.println(paper.getMin());
    }
}

class Paper{
    int min = Integer.MAX_VALUE;
    int [][]map = new int[12][12];
    int []remain = {0, 5, 5, 5, 5, 5};

    public Paper() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for(int i = 1;i <= 10;i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 1;j <= 10;j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }
    }

    public int getMin(){
        return min;
    }

    // 1을 만나는 순간 해당 위치에서 놓을 수 있는
    // 가장 큰 크기의 색종이부터 놓으면서 진행
    // 모든 1에 대해서 5x5 ... 1x1 색종이까지 BackTracking 방식으로 진행
    public void backTracking(int nowX, int nowY, int ans){
        // X가 범위를 벗어나면 다음 줄로 이동
        if(nowX >= 11){
            nowY++;
            nowX = 1;
        }

        // 종료조건 : 끝까지 모두 검사했을 때
        if(nowY >= 11){
            if(ans < min)
                min = ans;
            return;
        }

        if(map[nowY][nowX] == 0){
            backTracking(nowX + 1, nowY, ans);
        }else{
            for(int i = 5;i >= 1;i--){
                // ixi로 덮을 수 없는 경우
                if(!canCover(nowX, nowY, i))
                    continue;
                
                // 색종이의 수가 부족할 경우
                if(remain[i] <= 0)
                    continue;
                
                // 색종이로 덮고 다음 경우로 넘어가기
                fillMap(nowX, nowY, i, 0);
                remain[i]--;
                backTracking(nowX + i, nowY, ans + 1);
                
                // 이전 Case에 대해 돌아왔을때 상태 복구
                fillMap(nowX, nowY, i, 1);
                remain[i]++;
            }
        }
    }

    
    // 색종이로 덮을 수 있는지 여부 검사
    boolean canCover(int nowX, int nowY, int N){
        if(nowX + N - 1 > 10 || nowY + N - 1 > 10)
            return false;

        for(int i = 0;i < N;i++)
            for(int j = 0;j < N;j++)
                if(map[nowY + i][nowX + j] == 0)
                    return false;
        return true;
    }

    // num으로 NxN만큼 map을 덮는 메소드
    void fillMap(int nowX, int nowY, int N, int num){
        for(int i = 0;i < N;i++)
            for(int j = 0;j < N;j++)
                map[nowY + i][nowX + j] = num;
    }
}