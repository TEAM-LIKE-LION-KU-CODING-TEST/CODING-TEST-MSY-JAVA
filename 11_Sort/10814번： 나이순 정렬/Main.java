/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10814                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10814                          #+#        #+#      #+#    */
/*   Solved: 2025/02/06 22:10:52 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st;
        Member[] member = new Member[N];
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            member[i] = new Member(i, Integer.parseInt(st.nextToken()), st.nextToken());
        }

        Arrays.sort(member, comp);

        for(int i = 0;i < N;i++)
            member[i].toString(bw);
        bw.flush();
    }

    static Comparator<Member> comp = new Comparator<Member>() {
		@Override
		public int compare(Member m1, Member m2) {
			if(m1.getAge() > m2.getAge()){
                return 1;
            }else if(m1.getAge() == m2.getAge()){
                if(m1.getIndex() > m2.getIndex())
                    return 1;
                else if(m1.getIndex() == m2.getIndex())
                    return 0;
                else
                    return -1;
            }else{
                return -1;
            }
		}
	};
}

class Member{
    int index;
    int age;
    String name;

    public Member(int index, int age, String name){
        this.index = index;
        this.age = age;
        this.name = name;
    }

    public int getIndex(){
        return index;
    }

    public int getAge(){
        return age;
    }

    public void toString(BufferedWriter bw) throws IOException{
        bw.write("" + age + " " + name + "\n");
    }
}