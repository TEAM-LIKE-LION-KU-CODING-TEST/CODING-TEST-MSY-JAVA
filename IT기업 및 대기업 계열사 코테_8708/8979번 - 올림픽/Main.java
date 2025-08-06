/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 8979                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/8979                           #+#        #+#      #+#    */
/*   Solved: 2025/07/04 13:01:59 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    static class Country{
        public int cNum;
        public int gold;
        public int silver;
        public int bronze;

        public Country(int cNum, int gold, int silver, int bronze){
            this.cNum = cNum;
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
        }
    }

    private static boolean isSame(Country c1, Country c2){
        if((c1.gold == c2.gold) && (c1.silver == c2.silver) && (c1.bronze == c2.bronze))
            return true;
        return false;
    }

    private static void printCountry(Country[]arr, int N){
        for(int i = 0;i < N;i++)
            System.out.println(arr[i].cNum + " " + arr[i].gold 
                + " " + arr[i].silver + " " + arr[i].bronze);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Country[]country = new Country[N];
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            country[i] = new Country(
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken()), 
                Integer.parseInt(st.nextToken()), 
                Integer.parseInt(st.nextToken())
            );
        }

        Arrays.sort(country, comp);
        
        int[]rank = new int[N];
        int curRank = 1;
        int sameCumulate = 1;
        Country curCountry = country[0];
        rank[0] = curRank;
        for(int i = 1;i < N;i++){
            if(isSame(curCountry, country[i])){
                rank[i] = curRank;
                sameCumulate++;
                continue;
            }
            curRank+=sameCumulate;
            curCountry = country[i];
            rank[i] = curRank;
            sameCumulate = 1;
        }

        for(int i = 0;i < N;i++){
            if(country[i].cNum == K){
                bw.write("" + rank[i]);
                break;
            }
        }
        bw.flush();
    }

    static Comparator<Country>comp = new Comparator<Country> (){
      @Override
      public int compare(Country c1, Country c2){
        if(c1.gold < c2.gold) return 1;
        if(c1.gold > c2.gold) return -1;
        if(c1.silver < c2.silver) return 1;
        if(c1.silver > c2.silver) return -1;
        if(c1.bronze < c2.bronze) return 1;
        if(c1.bronze > c2.bronze) return -1;
        return 0;
      }  
    };
}