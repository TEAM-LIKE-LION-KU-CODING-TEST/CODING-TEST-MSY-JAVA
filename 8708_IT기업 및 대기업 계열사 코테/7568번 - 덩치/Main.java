/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 7568                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/7568                           #+#        #+#      #+#    */
/*   Solved: 2025/07/07 14:22:16 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    static class Person{
        public int idx;
        public int weight;
        public int height;
        public int rank;

        public Person(int idx, int weight, int height){
            this.idx = idx;
            this.weight = weight;
            this.height = height;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        Person[] persons = new Person[N];

        StringTokenizer st;
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            persons[i] = new Person(
                i,
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken())
            );
        }

        Arrays.sort(persons, comp);
        
        // 올바른 순위는 모든 사람 쌍을 비교해야 얻을 수 있음
        for(int i = 0;i < N;i++){
            int rank = 1;
            for(int j = 0;j < N;j++){
                if(persons[j].weight > persons[i].weight && persons[j].height > persons[i].height)
                    rank++;
            }
            persons[i].rank = rank;
        }

        for(int i = 0;i < N;i++){
            for(int j = 0;j < N;j++){
                if(persons[j].idx == i){
                    bw.write("" + persons[j].rank + " ");
                    break;
                }
            }
        }
        bw.flush();
    }

    // Comparator가 동등하지 않은 객체를 비교할 때도 0을 반환하여 비대칭/비전이성을 깨뜨림
    // Java 7 이상 TimSort가 이 비일관성을 검사하다가
    // Arrays.sort(persons, comp) 호출 시 IllegalArgumentException을 던지게 됨
    static Comparator<Person>comp = new Comparator<Person> (){
        @Override
        public int compare(Person p1, Person p2){
            if (p1.weight != p2.weight) 
                return p2.weight - p1.weight;  // 체중 내림차순
            return p2.height - p1.height;      // 키 내림차순
        }
    };
}