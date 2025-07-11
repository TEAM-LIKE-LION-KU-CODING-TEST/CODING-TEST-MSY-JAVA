/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 17266                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/17266                          #+#        #+#      #+#    */
/*   Solved: 2025/07/11 13:43:56 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[]road = new int[N + 1];
        for(int i = 0;i < N;i++)
            road[i] = 0;
        
        int M = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0;i < M;i++)
            road[Integer.parseInt(st.nextToken())] = 1;

        ////////
        // 시작-가로등-끝 사이 최대 구간을 찾기
        // 시작-가로등 or 가로등-끝의 경우 /2 를 하면 안되기 때문에
        // 별도로 기록하며 이때 무조건적으로 커버해야 하는 영역을 별도로 구하고 비교
        int singleMax = -1;
        int maxLen = -1;
        int nowLen = 1;
        // 시작-가로등 길이
        int idx = 0;
        while(true){
            if(road[idx] == 1){
                singleMax = idx;
                break;
            }
            idx++;
        }
        // 가로등-가로등 길이
        for(int i = idx + 1;i < N;i++){
            if(road[i] == 1){
                if(maxLen < nowLen)
                    maxLen = nowLen;
                nowLen = 1;
                continue;
            }
            nowLen++;
        }
        // 가로등-끝 길이
        if(singleMax < nowLen)
            singleMax = nowLen;

        ////////
        // 시작-가로등 or 가로등-끝의 최대와 가로등-가로등 커버를 위한 높이의 최대를 비교
        if(maxLen == -1 || singleMax > ((maxLen / 2) + (maxLen % 2))){
            System.out.println(singleMax);
        }else{
            // 홀수일때 /2보다 1개 더 많아야 하기 때문에
            System.out.println((maxLen / 2) + (maxLen % 2));
        }

    }
}

/*
8
2
3 7

3
*/