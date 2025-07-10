/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 9017                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/9017                           #+#        #+#      #+#    */
/*   Solved: 2025/07/10 15:03:41 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    private static class Pair {
        public int playerNum;
        public int totalScore;
        public int fifthScore;

        public Pair(int playerNum, int totalScore, int fifthScore){
            this.playerNum = playerNum;
            this.totalScore = totalScore;
            this.fifthScore = fifthScore;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        StringTokenizer st;
        for(int t = 0;t < T;t++){
            HashMap<Integer, Pair>teams = new HashMap<>();
            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());

            ////////
            // 배열로 입력받아 우선 각 팀원의 수를 누적
            int[]arr = new int[N + 1];
            for(int i = 1;i <= N;i++){
                int now = Integer.parseInt(st.nextToken());
                arr[i] = now;

                if(!teams.containsKey(now))
                    teams.put(now, new Pair(1, i, 0));
                else{
                    Pair tmp = teams.get(now);
                    tmp.playerNum += 1;
                    // Pair는 가변 객체이므로 replace 불필요
                    // teams.replace(now, tmp);
                }
            }

            ////////
            // HashMap의 keySet 정의
            Set<Integer>keys = teams.keySet();
            // 6명이 넘지 않는 팀의 팀원들의 순위를 제거하고
            // 수정된 배열에 기록
            int adjustedLen = 0;
            for(int key : keys){
                Pair tmp = teams.get(key);
                if(tmp.playerNum < 6){
                    for(int j = 1;j <= N;j++){
                        if(arr[j] == key){
                            arr[j] = 0;
                            adjustedLen++;
                        }
                    }
                }
            }
            int idx = 1;
            int[]adjustedArr = new int[N - adjustedLen + 1];
            for(int i = 1;i <= N;i++){
                if(arr[i] != 0)
                    adjustedArr[idx++] = arr[i];
            }
            N -= adjustedLen;

            ////////
            // 수정된 배열을 순회하며 HashMap을 통해
            // 해당 팀의 총 점수, 5번째 팀원 점수 갱신
            teams.clear();
            for(int i = 1;i <= N;i++){
                int now = adjustedArr[i];
                if(!teams.containsKey(now))
                    teams.put(now, new Pair(1, i, 0));
                else{
                    Pair tmp = teams.get(now);
                    tmp.playerNum += 1;
                    // 상위 네명의 점수를 누적
                    if(tmp.playerNum < 5)
                        tmp.totalScore += i;
                    else if(tmp.playerNum == 5)
                        tmp.fifthScore = i;
                }
            }
            keys = teams.keySet();

            ////////
            // Iterator 선언 시 제네릭 타입을 명확히 지정
            Iterator<Integer>iter = keys.iterator();
            // 순회하면서 최솟값을 찾고 기록
            int min = Integer.MAX_VALUE;
            Set<Integer>minTeams = new HashSet<>();
            while(iter.hasNext()){
                int key = iter.next();
                Pair tmp = teams.get(key);

                if(tmp.totalScore < min){
                    // 최솟값을 발견할 때마다 minTeams 초기화
                    minTeams.clear();
                    min = tmp.totalScore;
                    minTeams.add(key);
                }else if(tmp.totalScore == min){
                    minTeams.add(key);
                }
            }

            ////////
            // 만약 minTeams가 1개라면
            if(minTeams.size() == 1)
                bw.write("" + minTeams.iterator().next() + "\n");
            else{
                // 만약 minTeams가 여러개라면
                min = Integer.MAX_VALUE;
                int minIdx = 0;
                for(int key : minTeams){
                    int curFifth = teams.get(key).fifthScore;
                    if(curFifth < min){
                        min = curFifth;
                        minIdx = key;
                    }
                }
                bw.write("" + minIdx + "\n");
            }
        }
        bw.flush();
    }
}