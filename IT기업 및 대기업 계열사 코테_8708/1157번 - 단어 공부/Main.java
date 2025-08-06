/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1157                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1157                           #+#        #+#      #+#    */
/*   Solved: 2025/07/03 12:03:47 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;

class Main{
    static int ALPHABET_LENGTH = 26;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        // 소문자로 변환
        input = input.toLowerCase();
        int[]arr = new int[27];
        int N = input.length();

        for(int i = 0;i < ALPHABET_LENGTH;i++)
            arr[i] = 0;

        // ASCII 코드로 변환했을 때
        // a: 49, z: 74
        // -49 이후 a: 0, z:25
        for(int i = 0;i < N;i++)
            arr[(input.charAt(i) - '0') - 49]++;

        int max = -1;
        int maxIdx = 0;
        for(int i = 0;i < ALPHABET_LENGTH;i++)
            if(max < arr[i]){
                max = arr[i];
                maxIdx = i;
            }

        int maxCnt = 0;
        for(int i = 0;i < ALPHABET_LENGTH;i++){
            if(max == arr[i])
                maxCnt++;
            if(maxCnt >= 2){
                System.out.println("?");
                break;
            }
        }
        
        if(maxCnt == 1)
            System.out.println(Character.toUpperCase(Character.toChars(maxIdx + '0' + 49)[0]));
    }
}