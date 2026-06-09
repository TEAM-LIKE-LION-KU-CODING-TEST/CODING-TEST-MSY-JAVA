/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 25757                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/25757                          #+#        #+#      #+#    */
/*   Solved: 2025/07/08 12:34:32 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        HashMap<String,Boolean>hm = new HashMap<String,Boolean>();

        int peopleCnt = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        String game = st.nextToken();
        for(int i = 0;i < N;i++){
            String person = br.readLine();
            if(!hm.containsKey(person)){
                peopleCnt++;
                hm.put(person, true);
            }
        }

        switch (game) {
            case "Y":
                peopleCnt /= (2 - 1);
                break;
            case "F":
                peopleCnt = peopleCnt / (3 - 1);
                break;
            default:
                peopleCnt = peopleCnt / (4 - 1);
                break;
        }
        bw.write("" + peopleCnt);
        bw.flush();
    }
}