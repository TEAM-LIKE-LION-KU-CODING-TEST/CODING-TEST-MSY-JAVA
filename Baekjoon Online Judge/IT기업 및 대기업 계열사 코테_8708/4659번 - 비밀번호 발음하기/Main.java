/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 4659                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/4659                           #+#        #+#      #+#    */
/*   Solved: 2025/07/07 15:25:37 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;

class Main{
    private static boolean rule1(String pw){
        if(pw.contains("a") || pw.contains("e") || pw.contains("i") ||
            pw.contains("o") || pw.contains("u"))
            return true;
        return false;
    }

    private static boolean isGather(char c){
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            return true;
        return false;
    }

    private static boolean rule2(String pw){
        int cnt = 1;
        boolean nowGather = isGather(pw.charAt(0));
        for(int i = 1;i < pw.length();i++){
            if(nowGather == isGather(pw.charAt(i))){
                cnt++;
                if(cnt == 3)
                    return false;
            }else{
                nowGather = isGather(pw.charAt(i));
                cnt = 1;
            }
        }
        return true;
    }

    private static boolean rule3(String pw){
        for(int i = 1;i < pw.length();i++){
            if(pw.charAt(i) == 'e' || pw.charAt(i) == 'o')
                continue;
            if(pw.charAt(i) == pw.charAt(i - 1))
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while(true){
            String pw = br.readLine();
            if(pw.equals("end"))
                break;
            if(!rule1(pw) || !rule2(pw) || !rule3(pw)){
                bw.write("<" + pw + "> is not acceptable.\n");
                continue;
            }
            bw.write("<" + pw + "> is acceptable.\n");
        }
        bw.flush();
    }
}