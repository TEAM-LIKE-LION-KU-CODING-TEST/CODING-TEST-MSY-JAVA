package WEEK2_LINKED_LIST;
import java.io.*;
import java.util.*;

public class boj1158 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        LinkedList<Integer> list = new LinkedList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        for(int i = 0;i < N;i++)
            list.add(i + 1);
        
        bw.write("<");
        bw.flush();
        // 만약 K가 전체 사람 수보다 클 경우 처리
        int now = (K - 1) % list.size();
        for(int i = 0;i < N - 1;i++){
            bw.write(list.remove(now) + ", ");
            bw.flush();
            
            // 사람이 제거되었으므로 1을 빼서 순서 유지
            now += K - 1;
            // now == list.size()일 경우
            // 첫 번째 (현재 0번) 사람을 제거해야 한다
            if(now >= list.size())
                now %= list.size();
        }
        bw.write(list.get(0) + ">");
        bw.flush();

        br.close();
        bw.close();
    }
}