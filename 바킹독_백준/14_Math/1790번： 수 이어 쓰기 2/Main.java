/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1790                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: judemin <boj.kr/u/judemin>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1790                           #+#        #+#      #+#    */
/*   Solved: 2024/11/17 11:15:38 by judemin       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
import java.io.*;
import java.util.*;

class Main{
    public static void main(String [] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long num = Long.parseLong(st.nextToken());
		long k = Long.parseLong(st.nextToken());
		
		long result = 0;
		long cnt = 1;
		long length = 10;
		long tmp = k == 1 ? 1 : -1;
		
		for(int i = 1 ; i <= num + 1 ; i++) {
			if(result >= k) {
				tmp = i - 1;
				break;
			} else if(i == length) {
				cnt++;
				length *= 10;
			}
			
			result += cnt;
		}
		
		if(tmp != -1) {
			String str = tmp + "";
			System.out.println(str.charAt((int)(str.length() - (result - k) - 1)));
		} else {
			System.out.println(-1);
		}
    }
}