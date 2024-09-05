import java.io.*;
import java.util.*;

public class boj5397 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        for(int i = 0;i < N;i++){
            LinkedList<Character> list = new LinkedList<>();
            String st = br.readLine();

            // ListIterator를 활용하는 것이 중요
            ListIterator<Character> listIter = list.listIterator();
            for(int j = 0;j < st.length();j++){
                char c = st.charAt(j);
                switch(c){
                    case '<':
                        if(listIter.hasPrevious())
                            listIter.previous();
                        break;
                    case '>':
                        if(listIter.hasNext())
                            listIter.next();
                        break;
                    case '-':
                        if(listIter.hasPrevious()){
                            listIter.previous();
                            listIter.remove();
                        }
                        break;
                    default:
                        listIter.add(c);
                        break;
                }
            }

            Iterator<Character> iter = list.iterator();
            iter = list.iterator();
            while(iter.hasNext())
                bw.write(iter.next());
            bw.write("\n");
            bw.flush();
        }
    }
}

/*
2
<<BP<A>>Cd-
ThIsIsS3Cr3t

// 25% 오류가 발생하는 예제
1
abc<<<---def
*/