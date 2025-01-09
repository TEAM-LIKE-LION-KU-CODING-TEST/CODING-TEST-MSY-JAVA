/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 6198                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/6198                           #+#        #+#      #+#    */
/*   Solved: 2025/01/04 21:21:24 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.Stack;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Integer 범위를 넘어가기 때문에 Long 활용
        long result = 0;
        Stack<Long> input = new Stack<>();
        Stack<Pair> st = new Stack<>();

        int N = Integer.parseInt(br.readLine());
        for(int i = 0;i < N;i++)
            input.add(Long.parseLong(br.readLine()));

        // 정원관리사가 오른쪽을 보기 때문에
        // 역순으로 계산
        for(int i = 0;i < N;i++){
            long height = input.pop();

            Pair p = new Pair(height);
            while(true){
                // Stack이 비어있거나 Top이 나보다 크거나 같을 때까지
                if(st.isEmpty() || st.peek().getHeight() >= height)
                    break;

                Pair popPair = st.pop();
                long popSum =  popPair.getSum();

                // result에 누적시킴과 동시에
                result += popSum;
                // pop된 Pair의 누적값은 현재 height보다 작은 pair의 누적값이므로
                // 현재 Pair에도 pop된 Pair의 누적값을 추가
                p.incSum(1 + popSum);
            }
            st.add(p);
            //System.out.println(i + " s: " + st.size() + " h: " + height +
            //    " top: " + st.peek() + " r: " + result);
        }

        // 마지막에 Stack 남은 요소들의 누적값을 모두 더해준다
        while(!st.isEmpty()) 
            result += st.pop().getSum();
        
        System.out.println(result);
    }
}

class Pair{
    // 높이
    long height;
    // 누적값
    long sum;

    public Pair(long height){
        this.height = height;
        this.sum = 0;
    }

    public void incSum(long tmp){
        this.sum += tmp;
    }

    public long getHeight(){
        return this.height;
    }

    public long getSum(){
        return this.sum;
    }

    public String toString(){
        return "[h:" + height+ " s:" + sum + "]";
    }
}


/*
8
8
6
4
3
5
4
3
7
-
16

10
5
1
4
1
3
1
2
1
1
1
-
24
*/