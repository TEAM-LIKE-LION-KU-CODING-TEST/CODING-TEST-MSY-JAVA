/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1406                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1406                           #+#        #+#      #+#    */
/*   Solved: 2025/01/03 15:27:10 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String result = br.readLine();
        int M = Integer.parseInt(br.readLine());
        
        LinkedList<Character> ll = new LinkedList<>();
        for(int i = 0;i < result.length();i++)
            ll.add(result.charAt(i));

        // ListIterator를 사용하여 LinkedList 내에서 이동
        ListIterator<Character> listIter = ll.listIterator();
        // 커서를 맨 뒤로 이동
        while(listIter.hasNext())
            listIter.next();
        
        for(int i = 0;i < M;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            switch (st.nextToken().charAt(0)){
                case 'L':
                    if(listIter.hasPrevious())
                        listIter.previous();
                    break;
                case 'D':
                    if(listIter.hasNext())
                        listIter.next();
                    break;
                case 'B':
                    if(listIter.hasPrevious()){
                        listIter.previous();
                        listIter.remove();
                    }
                    break;
                case 'P':
                    char input = st.nextToken().charAt(0);
                    listIter.add(input);

                    break;
            }
            // printLinkedList(ll, bw);
            // System.out.println("--" + (i + 1));
        }

        printLinkedList(ll, bw);
    }

    // 디버깅을 위한 출력 메소드드
    private static void printLinkedList(LinkedList<Character> ll, BufferedWriter bw) throws IOException{
        Iterator<Character> iter = ll.iterator();
        while(iter.hasNext()){
            char c = iter.next();
            bw.write(c);
        }
        bw.flush();
    }
}

// abcdx*
// abcdx